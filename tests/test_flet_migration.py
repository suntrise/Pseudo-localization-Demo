"""Exercise real Flet controls and serialization without launching a client."""

import asyncio
import dataclasses
import inspect
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

import flet as ft
import httpx
import msgpack
from flet.messaging.connection import Connection
from flet.messaging.session import Session
from flet.messaging.protocol import configure_encode_object_for_msgpack
from flet.pubsub.pubsub_hub import PubSubHub

import pslo
import pslo_mini
from lib import controls, pslo_work, update


class MemoryConnection(Connection):
    def send_message(self, message):
        msgpack.packb(message, default=configure_encode_object_for_msgpack(ft.BaseControl))


def walk(control):
    yield control
    if not dataclasses.is_dataclass(control):
        return
    for field in dataclasses.fields(control):
        if field.name.startswith("_"):
            continue
        value = getattr(control, field.name)
        for child in value if isinstance(value, list) else [value]:
            if isinstance(child, ft.BaseControl):
                yield from walk(child)


async def click(control):
    result = control.on_click(None)
    if inspect.isawaitable(result):
        await result


class MigrationTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.sessions = []
        self.logging = patch("lib.log.out")
        self.logging.start()
        self.addCleanup(self.logging.stop)

    def build(self, app=pslo, platform=ft.PagePlatform.WINDOWS, web=False):
        connection = MemoryConnection()
        connection.loop = asyncio.get_running_loop()
        connection.pubsubhub = PubSubHub(connection.loop)
        session = Session(connection)
        self.sessions.append(session)
        session.attach_connection(connection)
        page = session.page
        page.platform = platform
        page.web = web
        app.main(page)
        msgpack.packb(session.get_page_patch(),
                      default=configure_encode_object_for_msgpack(ft.BaseControl))
        return page

    def find(self, page, cls, **attrs):
        return next(c for root in page.controls for c in walk(root)
                    if isinstance(c, cls)
                    and all(getattr(c, k, None) == v for k, v in attrs.items()))

    def fields(self, page):
        source = self.find(page, ft.TextField, hint_text="在这里输入要翻译的内容~")
        result = self.find(page, ft.TextField, read_only=True)
        return source, result

    async def test_both_apps_construct_and_serialize_on_all_targets(self):
        for app in (pslo, pslo_mini):
            for platform, web in [(ft.PagePlatform.WINDOWS, False),
                                  (ft.PagePlatform.LINUX, False),
                                  (ft.PagePlatform.MACOS, False),
                                  (ft.PagePlatform.ANDROID, False),
                                  (ft.PagePlatform.IOS, False),
                                  (ft.PagePlatform.MACOS, True)]:
                with self.subTest(app=app.__name__, platform=platform, web=web):
                    page = self.build(app, platform, web)
                    self.assertTrue(page.controls)
                    self.assertEqual(page.window.width is None, web or platform.is_mobile())
                    if web:
                        self.assertFalse(any(isinstance(c, ft.WindowDragArea)
                                             for root in page.controls for c in walk(root)))

    async def test_mini_conversion_has_complete_arguments_and_copy_action(self):
        page = self.build(pslo_mini)
        source, result = self.fields(page)
        source.value = "Hello 123"
        await click(self.find(page, ft.FilledTonalButton, content="伪本地化!"))
        self.assertTrue(result.value)
        self.assertNotEqual(result.value, source.value)
        copy = self.find(page, ft.IconButton, icon=ft.Icons.COPY_OUTLINED)
        self.assertEqual(copy.action.data, result.value)
        source.value = ""
        await click(self.find(page, ft.FilledTonalButton, content="伪本地化!"))
        self.assertEqual(result.value, "")

    async def test_history_clear_and_session_isolation(self):
        page = self.build()
        source, result = self.fields(page)
        convert = self.find(page, ft.FilledButton, content="进行伪本地化!")
        source.value = "first"
        await click(convert)
        history = self.find(page, ft.TextButton, content="复制全部")
        self.assertIn("first →", history.action.data)
        await click(self.find(page, ft.TextButton, content="清空"))
        dialog = page._dialogs.controls[-1]
        await click(dialog.actions[0])
        self.assertEqual(history.action.data, "")
        source.value = "second"
        await click(convert)
        self.assertNotIn("first →", history.action.data)
        self.assertIn("second →", history.action.data)
        other = self.build()
        self.assertEqual(self.find(other, ft.TextButton, content="复制全部").action.data, "")

    async def test_select_events_and_invalid_numeric_inputs(self):
        page = self.build()
        suffix = self.find(page, ft.Dropdown, label="前后缀")
        suffix.value = "4"
        suffix.on_select(None)
        interval = self.find(page, ft.TextField, label="每隔多少个字符重复一次：")
        interval.value = "0"
        interval.on_blur(None)
        self.assertEqual(interval.value, "7")
        theme = self.find(page, ft.Dropdown, label="亮暗模式")
        theme.value = "1"
        theme.on_select(None)
        self.assertEqual(page.theme_mode, ft.ThemeMode.DARK)
        source, result = self.fields(page)
        source.value = "Test"
        await click(self.find(page, ft.FilledButton, content="进行伪本地化!"))
        self.assertTrue(result.value.startswith("["))

    async def test_native_import_bytes_path_cancel_and_invalid_utf8(self):
        page = self.build()
        source, result = self.fields(page)
        button = self.find(page, ft.IconButton, tooltip="导入文本文件")
        with patch.object(ft.FilePicker, "pick_files", new_callable=AsyncMock) as picker:
            picker.return_value = [ft.FilePickerFile(1, "input.txt", 6, bytes=b"\xef\xbb\xbfabc")]
            await click(button)
            self.assertEqual(source.value, "abc")
            self.assertTrue(picker.await_args.kwargs["with_data"])
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "input.txt"
                path.write_text("from path", encoding="utf-8")
                picker.return_value = [ft.FilePickerFile(1, path.name, 9, path=str(path))]
                await click(button)
                self.assertEqual(source.value, "from path")
            picker.return_value = []
            await click(button)
            self.assertEqual(source.value, "from path")
            picker.return_value = [ft.FilePickerFile(1, "bad.txt", 1, bytes=b"\xff")]
            await click(button)
            self.assertIn("导入失败", page._dialogs.controls[-1].content.value)

    async def test_web_import_action_and_download_bytes(self):
        page = self.build(web=True)
        button = self.find(page, ft.IconButton, tooltip="导入文本文件")
        self.assertIsInstance(button.action, ft.PickFiles)
        self.assertTrue(button.action.with_data)
        self.assertIsNone(button.on_click)
        picker = button.action.file_picker
        event = ft.FilePickerResultEvent(
            control=picker, name="result", data=None,
            files=[ft.FilePickerFile(1, "web.txt", 3, bytes=b"abc")],
        )
        await picker.on_result(event)
        source, result = self.fields(page)
        self.assertEqual(source.value, "abc")
        await click(self.find(page, ft.IconButton, tooltip="保存文本"))
        dialog = page._dialogs.controls[-1]
        group = next(c for c in walk(dialog) if isinstance(c, ft.RadioGroup))
        group.value = "1"
        with patch.object(ft.FilePicker, "save_file", new_callable=AsyncMock) as save:
            save.return_value = None
            await click(dialog.actions[0])
            self.assertEqual(save.await_args.kwargs["src_bytes"],
                             ("abc\n" + result.value).encode("utf-8"))
            self.assertEqual(save.await_args.kwargs["file_type"], ft.FilePickerFileType.CUSTOM)
            self.assertTrue(save.await_args.kwargs["file_name"].endswith(".txt"))

    async def test_window_buttons_use_mounted_page_and_await_close(self):
        page = self.build()
        maximize = self.find(page, controls.MaximizeButton)
        await click(maximize)
        self.assertTrue(page.window.maximized)
        await click(maximize)
        self.assertFalse(page.window.maximized)
        await click(self.find(page, controls.MinimizeButton))
        self.assertTrue(page.window.minimized)
        with patch.object(ft.Window, "close", new_callable=AsyncMock) as close:
            await click(self.find(page, controls.CloseButton))
            close.assert_awaited_once()

    async def test_conversion_edge_cases(self):
        options = ("enxa", "deft", "0", "0", "0", "", "", "", "7", False, "5", True)
        for text in ("", "null", "%", "\\", "%s\\n\\r"):
            with self.subTest(text=text):
                self.assertIsInstance(pslo_work.pslo(text, *options), str)
        result = pslo_work.pslo("abc123", "enxa", "deft", "1", "0", "0",
                                "", "", "", "7", False, "5", False)
        self.assertTrue(result.endswith("①②③"))
        self.assertNotEqual(result[:3], "abc")

    async def test_update_network_errors_empty_releases_and_prerelease(self):
        for payload, expected in [([], "ERR"), ({"message": "rate limit"}, "ERR"),
                                  ([{"tag_name": "v5.0.0p"}], "NUL"),
                                  ([{"tag_name": "v6", "body": None, "prerelease": True}], "预发布")]:
            with self.subTest(payload=payload):
                transport = httpx.MockTransport(lambda request: httpx.Response(200, json=payload))
                client = httpx.AsyncClient(transport=transport)
                with patch("lib.update.httpx.AsyncClient", return_value=client):
                    response = await update.update("v5.0.0p")
                self.assertIn(expected, response)
        with patch("lib.update.httpx.AsyncClient.get", new_callable=AsyncMock,
                   side_effect=httpx.ConnectError("offline")):
            self.assertEqual(await update.update("v5.0.0p"), "ERR")


if __name__ == "__main__":
    unittest.main()
