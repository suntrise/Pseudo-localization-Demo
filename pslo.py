import flet as ft # 界面库
import asyncio
from pathlib import Path
import sys # 系统库
import datetime # 日期时间库
from lib import log # 日志输出库
from lib import pslo_work # 工作模块
from lib import update # 更新模块
from lib import controls # 组件拓展库
from lib import basic_info # 基础信息
# from lib import config_li # 写入配置库, 尚未完成

# 基础信息位于lib/basic_info.py

# 基本输出
log.out(0, "Python version: " + sys.version)
log.out(0, "PSLO version: " + basic_info.ver)

# 主程序
def main(page: ft.Page):
    pshis = ""
    desktop = not page.web and not page.platform.is_mobile()
    page.title = basic_info.title
    if desktop:
        page.window.left = 200
        page.window.top = 100
        page.window.height = 600
        page.window.width = 900
        page.window.min_height = 500
        page.window.min_width = 882
        page.window.title_bar_hidden = True

    def notify(message):
        page.show_dialog(ft.SnackBar(ft.Text(message)))

    # 字符相隔位数是否数字确定
    def ccs_check(e):
        if not str(cus_cs.value).isdecimal() or int(cus_cs.value) < 1:
            cus_cs.value = "7"
            log.out(0, "Set the CUS value to 7. Content: " + str(cus_cs.value))
        page.update()

    # 是否显示前后缀配置栏
    def psf_check(e):
        if suf_way.value == "4":
            cus_ps.visible = True
            log.out(0, "CUS Toolbar visible is true")
        else:
            cus_ps.visible = False
            log.out(0, "CUS Toolbar visible is false")
        page.update()

    # 原pslo函数已迁移至lib/pslo_work.py

    # 转换任务放到工作线程，避免阻塞 Flet 1.0 的事件循环。
    async def pslo(e):
        nonlocal pshis
        ccs_check(e)
        ws_check(e)
        vcs_check(e)
        source = pstype.value or ""
        options = (source, xab.value, uplw.value, num_pslo.value,
                   vowel_cs.value, suf_way.value, cus_pre.value or "",
                   cus_suf.value or "", cus_re.value or "", cus_cs.value,
                   hash_cb.value, hash_ws.value, vis_con_cb.value)
        pslo_btn.disabled = True
        page.update()
        try:
            if sys.platform == "emscripten":
                result.value = pslo_work.pslo(*options)
            else:
                result.value = await asyncio.to_thread(pslo_work.pslo, *options)
            pshis += source + " → " + result.value + " | " + datetime.datetime.now().strftime('%H:%M:%S') + "\n————————————————————————————————————\n"
            history.value = pshis
            copy_btn.action = ft.CopyToClipboard(result.value)
            copy_history_btn.action = ft.CopyToClipboard(history.value)
        finally:
            pslo_btn.disabled = False
            page.update()

    # 复制操作由客户端直接执行，以支持浏览器的用户手势权限。
    def copy_text(e):
        notify("已复制")

    def copy_history(e):
        notify("已复制历史记录")

    async def load_files(files):
        if not files:
            return
        selected = files[0]
        try:
            if selected.bytes is not None:
                text = selected.bytes.decode("utf-8-sig")
            elif selected.path:
                text = await asyncio.to_thread(Path(selected.path).read_text, encoding="utf-8-sig")
            else:
                notify("无法读取所选文件")
                return
            pstype.value = text
            await pslo(None)
            notify("已导入: " + selected.name)
        except (OSError, UnicodeError) as exc:
            notify("导入失败: " + str(exc))

    async def ps_files(e: ft.FilePickerResultEvent):
        # Web 的 PickFiles 客户端操作通过 on_result 返回内容。
        await load_files(e.files)

    async def pick_files(e):
        files = await file_picker.pick_files(
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["txt"], allow_multiple=False, with_data=True,
        )
        await load_files(files)

    async def save_text(text, filename):
        if not text:
            notify("没有可保存的内容")
            return
        try:
            path = await file_picker.save_file(
                file_name=filename, file_type=ft.FilePickerFileType.CUSTOM,
                allowed_extensions=["txt"], src_bytes=text.encode("utf-8"),
            )
            if path:
                notify("已保存至: " + path)
            elif page.web:
                notify("已发起下载")
        except (OSError, ValueError, ft.FletException) as exc:
            notify("保存失败: " + str(exc))

    async def sv_files(e):
        close_svw(e)
        text = result.value or ""
        if save_way_dd.value == "1":
            text = (pstype.value or "") + "\n" + text
        await save_text(text, "pseudo-localized.txt")

    async def sv_his(e):
        await save_text(pshis, "pseudo-history.txt")

    # 清除历史记录
    def clear_his(e):
        nonlocal pshis
        close_chq(e)
        pshis = ""
        history.value = "无记录"
        copy_history_btn.action = ft.CopyToClipboard("")
        log.out(1, "History is cleared")
        page.show_dialog(ft.SnackBar(ft.Text(f"已清空"))) # 提示栏
        page.update()
        log.out(0, "Snack bar pop-up(CH)")

    # Hash输入框解禁
    def hash_check(e):
        if hash_cb.value == True:
            hash_ws.disabled = False
            log.out(0, "Hash ID text field is enable")
        else:
            hash_ws.disabled = True
            log.out(0, "Hash ID text field is disabled")
        page.update()

    # Hash数值确认
    def ws_check(e):
        ws = hash_ws.value
        if str(ws).isdecimal() == False:
            hash_ws.value = "5"
            log.out(0, "Set the Hash ID text field value to 5. Content: " + str(ws))
        elif int(ws) < 3:
            hash_ws.value = "3"
            log.out(0, "The value is too small, has set the Hash ID text field value to 3. Content: " + str(ws))
        elif int(ws) > 10:
            hash_ws.value = "10"
            log.out(0, "The value is too big, has set the Hash ID text field value to 10. Content: " + str(ws))
        page.update()

    # 元音重复次数检测
    def vcs_check(e):
        vcs = vowel_cs.value
        if str(vcs).isdecimal() == False:
            vowel_cs.value = "0"
            log.out(0, "Set the Vowel repetition text field value to 0")
        elif int(vcs) < 0:
            vowel_cs.value = "0"
            log.out(0, "The value is too small, has set the Vowel repetition text field value to 0")
        elif int(vcs) > 10:
            vowel_cs.value = "10"
            log.out(0, "The value is too big, has set the Vowel repetition text field value to 10")
        page.update()

    # 明暗切换
    def theme_changed(e):
        if theme.value == "0":
            page.theme_mode = (
                ft.ThemeMode.LIGHT # 亮色
            )
            log.out(1, "Switch to LIGHT")
        if theme.value == "1":
            page.theme_mode = (
                ft.ThemeMode.DARK # 暗黑
            )
            log.out(1, "Switch to DARK")
        if theme.value == "2":
            page.theme_mode = (
                ft.ThemeMode.SYSTEM # 系统
            )
            log.out(1, "Switch to SYSTEM")
        page.update()

    # 色彩选择
    def sch_changed(e):
        sch = int(scheme.value)
        default_fontfamily = "Microsoft Yahei"
        if sch == 0:
            page.theme = ft.Theme(font_family = default_fontfamily,
                            color_scheme_seed = ft.Colors.BLUE) # 蓝色
            log.out(1, "Switch to color BLUE")
        if sch == 1:
            page.theme = ft.Theme(font_family = default_fontfamily,
                            color_scheme_seed = ft.Colors.PINK) # 粉色
            log.out(1, "Switch to color PINK")
        if sch == 2:
            page.theme = ft.Theme(font_family = default_fontfamily,
                            color_scheme_seed = ft.Colors.GREEN) # 绿色
            log.out(1, "Switch to color GREEN")
        if sch == 3:
            page.theme = ft.Theme(font_family = default_fontfamily,
                            color_scheme_seed = ft.Colors.BROWN) # 巧克力色
            log.out(1, "Switch to color BROWN")
        if sch == 4:
            page.theme = ft.Theme(font_family = default_fontfamily,
                            color_scheme_seed = ft.Colors.DEEP_PURPLE_100) # 紫色
            log.out(1, "Switch to color DEEP_PURPLE")
        page.update()

    # 透明度设置
    def opacity_slider_changed(e):
        opac_value = opacity_slider.value / 100
        page.window.opacity = opac_value
        log.out(1, "Window opacity: " + str(page.window.opacity))
        if opac_value <= 0.75:
            opac_warn_bar.visible = True
        else:
            opac_warn_bar.visible = False
        page.update()

    # 打开“什么是伪本地化”窗口
    def open_what(e):
        page.show_dialog(what_dlg)
        log.out(1, "Dialog open(WHT)")
        page.update()

    # 打开“确定清除历史记录”窗口
    def open_chq(e):
        page.show_dialog(chq_dlg)
        log.out(1, "Dialog open(CHQ)")
        page.update()

    # 打开“保存方式”窗口
    def open_svw(e):
        page.show_dialog(svw_dlg)
        log.out(1, "Dialog open(SVW)")
        page.update()

    # 打开“保存更新日志”窗口
    def open_upd(e):
        page.show_dialog(upd_dlg)
        log.out(1, "Dialog open(UPD)")
        page.update()

    # 关闭“什么是伪本地化”窗口
    def close_what(e):
        page.pop_dialog()
        log.out(1, "Dialog close(WHT)")
        page.update()

    # 关闭“确定清除历史记录”窗口
    def close_chq(e):
        page.pop_dialog()
        log.out(1, "Dialog close(CHQ)")
        page.update()

    # 关闭“保存方式”窗口
    def close_svw(e):
        page.pop_dialog()
        log.out(1, "Dialog close(SVW)")
        page.update()

    # 原check_for_update函数已迁移至lib/update.py

    # 检查更新
    async def check_for_update(e):
        # 关闭“发现更新”窗口
        def close_find_upd_dlg(e):
            page.pop_dialog()
            page.update()
            log.out(1, "Dialog close(UPD)")
        content = await update.update(basic_info.ver)
        if content == "ERR":
            page.show_dialog(ft.SnackBar(ft.Text(f"检查更新超时, 请检查网络连接"))) # 提示栏
            page.update()
            log.out(1, "Snack Bar pop-up(CUF)")
        elif content == "NUL":
            page.show_dialog(ft.SnackBar(ft.Text(f"你正在使用最新版本"))) # 提示栏
            log.out(1, "Snack Bar pop-up(VLT)")
            page.update()
        else:
            download_url = update.get_link()
            # 定义“发现更新”窗口
            find_upd_dlg = ft.AlertDialog(
                title = ft.Text("发现更新"), on_dismiss = lambda e: log.out(0, "Dialog dismissed(UPD)"),
                content = ft.Markdown(content, selectable = True),
                actions = [
                    ft.FilledButton("更新", icon = ft.Icons.UPLOAD_OUTLINED, url = download_url),
                    ft.TextButton("取消", icon = ft.Icons.CLOSE_OUTLINED, on_click = close_find_upd_dlg)
                ],
            )
            page.show_dialog(find_upd_dlg) # 打开“发现更新”窗口
            page.update()
            log.out(1, "Dialog open(UPD)")


    # 置顶
    def always_on_top(e):
        if page.window.always_on_top == False:
            page.window.always_on_top = True
            ontop_btn.icon = ft.Icons.PUSH_PIN_ROUNDED
            log.out(1, "Set always on top")
            page.show_dialog(ft.SnackBar(ft.Text(f"已置顶"))) # 提示栏
            log.out(1, "Snack Bar pop-up(AOT)")
            page.update()
        elif page.window.always_on_top == True:
            page.window.always_on_top = False
            ontop_btn.icon = ft.Icons.PUSH_PIN_OUTLINED
            log.out(1, "Cancel always on top")
            page.show_dialog(ft.SnackBar(ft.Text(f"已取消置顶"))) # 提示栏
            log.out(1, "Snack Bar pop-up(ATX)")
            page.update()

    # 主体内容控制
    def rail_ctrl(e):
        if rail.selected_index == 0:
            home_page.visible = True
            his_page.visible = False
            collection_page.visible = False
            set_page.visible = False
        elif rail.selected_index == 1:
            home_page.visible = False
            his_page.visible = True
            collection_page.visible = False
            set_page.visible = False
        elif rail.selected_index == 2:
            home_page.visible = False
            his_page.visible = False
            collection_page.visible = True
            set_page.visible = False
        elif rail.selected_index == 3:
            home_page.visible = False
            his_page.visible = False
            collection_page.visible = False
            set_page.visible = True
        log.out(0, "Rail Selected Index: " + str(rail.selected_index))
        page.update()

    # “什么是伪本地化”窗口定义
    what_dlg = ft.AlertDialog(
        title = ft.Text("什么是伪本地化?"), on_dismiss = lambda e: log.out(0, "Dialog dismissed(WHT)"),
        content = ft.Markdown(basic_info.what_text, selectable = True),
        actions = [
            ft.TextButton("我知道啦", icon = ft.Icons.DONE, on_click = close_what)
        ],
        actions_alignment = ft.MainAxisAlignment.END
    )

    # “确定清除历史记录”窗口定义
    chq_dlg = ft.AlertDialog(
        title = ft.Text("确定删除历史记录?"), on_dismiss = lambda e: log.out(0, "Dialog dismissed(CHQ)"),
        content = ft.Text("确定删除所有历史记录,?\n该操作不可逆!"),
        actions = [
            ft.Button("确定", icon = ft.Icons.DONE, on_click = clear_his, bgcolor = ft.Colors.RED, color=ft.Colors.WHITE, elevation = 0),
            ft.FilledTonalButton("取消", icon = ft.Icons.CLOSE, on_click = close_chq)
        ],
        actions_alignment = ft.MainAxisAlignment.END
    )

    # “保存方式”窗口定义
    save_way_dd = ft.RadioGroup(
    value = "0",content=ft.Column([
    ft.Radio(value = "0", label="只保存伪本地化的结果"),
    ft.Radio(value = "1", label="同时保存源文本和伪本地化结果"),
    ]))
    svw_dlg = ft.AlertDialog(
        title = ft.Text("保存方式"), on_dismiss = lambda e: log.out(0, "Dialog dismissed(SVW)"),
        content = ft.Column(controls = [ft.Text("您希望如何保存?"), save_way_dd], height = 100, width = 300),
        actions = [
            ft.FilledButton("确定", icon = ft.Icons.DONE, on_click = sv_files)
        ],
        actions_alignment = ft.MainAxisAlignment.END
    )


    # “更新日志”窗口定义
    upd_dlg = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Markdown(basic_info.updmd, selectable = True),
                ],
            ),
            padding = 20,
            expand = True,
        ),
        on_dismiss = lambda e: log.out(0, "Dialog dismissed(UPH)")
    )

    # 用户界面
    # 基本内容定义
    page.theme = ft.Theme(
         font_family = "Microsoft Yahei",
         color_scheme_seed = ft.Colors.BLUE
         )

    # 窗口区
    title_text = ft.Container(ft.Text(basic_info.title, size = 20))
    title_icon = ft.Container(ft.Icon(ft.Icons.LANGUAGE_OUTLINED), padding = 5)
    ontop_btn = ft.IconButton(icon = ft.Icons.PUSH_PIN_OUTLINED, on_click = always_on_top, tooltip = "置顶")
    more_options = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(content=ft.TextButton(
                "打开网页版", icon=ft.Icons.OPEN_IN_BROWSER,
                url="https://suntrise.github.io/pseudo/")),
            ft.PopupMenuItem(content=ft.TextButton(
                "打开项目仓库", icon=ft.Icons.COLLECTIONS_BOOKMARK_OUTLINED,
                url="https://github.com/suntrise/Pseudo-localization-Demo")),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(content="什么是伪本地化?",
                             icon=ft.Icons.QUESTION_MARK_OUTLINED, on_click=open_what),
        ],
        tooltip="更多选项",
    )

    if desktop and page.platform != ft.PagePlatform.MACOS:
        min_btn = controls.MinimizeButton( icon = ft.Icons.HORIZONTAL_RULE_ROUNDED)
        max_btn = controls.MaximizeButton( icon = ft.Icons.SQUARE_OUTLINED)
        close_btn = controls.CloseButton()
        titlebar_controls = [ontop_btn, more_options, min_btn, max_btn, close_btn]
    else:
        titlebar_controls = ([ontop_btn] if desktop else []) + [more_options]

    titlebar = ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        controls = [
            ft.Row(spacing = 1, controls = [title_icon, title_text]),
            ft.Row(spacing = 1,controls = titlebar_controls)
        ])
    if desktop:
        titlebar = ft.WindowDragArea(titlebar)
    # 主页区
    xab = ft.RadioGroup(value = "enxa", content = ft.Row(wrap = True, controls = [
    ft.Radio(value = "enxa", label = "en-XA (qps-ploc) (e.g. ab→ǻƀ)"),
    ft.Radio(value = "enxb", label = "en-XB (qps-plocm) (e.g. ab→ba)")]))
    XABrow = ft.Row(spacing = 1, controls = [ft.Text("伪本地化方式:", size = 15), xab], wrap = True)
    uplw = ft.RadioGroup(value = "deft", content = ft.Row([
    ft.Radio(value = "deft", label = "保持原样"),
    ft.Radio(value = "upper", label = "全部大写"),
    ft.Radio(value = "lower", label = "全部小写")]))
    ulrow = ft.Row(spacing = 1, controls = [ft.Text("大小写:", size = 15), uplw])
    pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size =15, multiline = True, max_lines = 5)
    result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = True, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
            "进行伪本地化!",
            icon = ft.Icons.TRANSLATE_OUTLINED,
            tooltip = "将您所填写的内容伪本地化, 每次生成结果都会不一样哦",
            on_click = pslo
        )
    copy_btn = ft.IconButton(
            ft.Icons.COPY,
            tooltip = "将生成内容添加到设备剪切板",
            action = ft.CopyToClipboard(""),
            on_click = copy_text
        )
    # 导入导出文件
    file_picker = ft.FilePicker(on_result=ps_files)
    import_btn = ft.IconButton(
        icon=ft.Icons.UPLOAD_FILE_OUTLINED, tooltip="导入文本文件",
        action=ft.PickFiles(
            file_picker, file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["txt"], with_data=True,
        ) if page.web else None,
        on_click=None if page.web else pick_files,
    )
    save_btn = ft.IconButton(
        icon=ft.Icons.SAVE_OUTLINED, tooltip="保存文本", on_click=open_svw,
    )
    pslo_row = ft.Row(spacing=10, controls=[pslo_btn, copy_btn, import_btn, save_btn])
    home_page = ft.Column(
        expand = True,
        horizontal_alignment = ft.CrossAxisAlignment.STRETCH,
        scroll = ft.ScrollMode.AUTO,
        controls = [XABrow, ulrow, pstype, result, pslo_row])
    history = ft.Text("无记录", size = 18, selectable = True)
    his_card = ft.Card(
            content = ft.Container(
                content = ft.Column(
                    [
                        history
                    ]
                ),
                expand = True,
                padding = 10,
            ),
            elevation = 0.5
        )
    his_title = ft.Row(controls = [
        ft.Icon(
            ft.Icons.LIST_ALT_OUTLINED
        ),
        ft.Text(
            "历史记录:",
            size = 20
        )])
    copy_history_btn = ft.TextButton(
        "复制全部", icon=ft.Icons.COPY_OUTLINED,
        action=ft.CopyToClipboard(""), on_click=copy_history,
    )
    his_opts = ft.Row(spacing=5, controls=[
        copy_history_btn,
        ft.TextButton("导出记录", icon=ft.Icons.SAVE_OUTLINED, on_click=sv_his),
        ft.TextButton("清空", icon=ft.Icons.DELETE_FOREVER_OUTLINED, on_click=open_chq),
    ])
    his_bar = ft.Row(alignment = ft.MainAxisAlignment.SPACE_BETWEEN, controls = [
        his_title,
        his_opts
    ])
    his_col = ft.Column(
                expand = True,
                scroll = ft.ScrollMode.ALWAYS,
                        controls = [
                        his_bar,
                        his_card
                    ]
                )
    his_page = ft.Container(content = his_col, visible = False, expand = True)

    # 集合区
    collection_unav_card = ft.Card(
        content = ft.Container(
                content = ft.Column(
                    [
                        ft.Icon(ft.Icons.ANNOUNCEMENT_OUTLINED, size = 56, tooltip = "这里将来会做一些集成脚本来快速实现某些功能"),
                        ft.Text("嘿, “集合”还在开发中, 暂时还不可用!", size = 18)
                    ]
                ),
                padding = 15
            ),
            elevation = 0.5
        )
    collection_page = ft.Container(content = collection_unav_card, visible = False, alignment = ft.Alignment.CENTER, expand = True)

    # 设置区
    # 伪本地化设置
    opt_pslo = ft.Row(
            [
                ft.Icon(icon = ft.Icons.TRANSLATE_OUTLINED),
                ft.Text("伪本地化", size = 22)
            ]
        )
    opt_pslo_detail = ft.Text("(部分选项仅适用于 en-XA)", size=15)
    #----------#
    suf_way = ft.Dropdown(
            label = "前后缀",
            value = "0",
            hint_text = "选择前后缀方案，默认为“不添加前后缀”",
            options = [
                ft.DropdownOption(key = "0", text = "不添加前后缀"),
                ft.DropdownOption(key = "1", text = "[中括号+感叹号括起来 (微软式伪本地化)!!!]"),
                ft.DropdownOption(key = "2", text = "[中括号+在语段后添加英文基数词 (安卓式伪本地化) one two three]"),
                ft.DropdownOption(key = "3", text = "[中括号+在语段后添加阿拉伯数字 12345]"),
                ft.DropdownOption(key = "4", text = "自定义前后缀")
           ], on_select = psf_check)
    cus_pre = ft.TextField(width = 80, label = "前缀", value = "[")
    cus_suf = ft.TextField(width = 80, label = "后缀", value = "]")
    cus_re = ft.TextField(label = "在语段后重复添加……")
    cus_cs = ft.TextField(width = 230, label = "每隔多少个字符重复一次：", value = "7", on_blur = ccs_check)
    cus_ps = ft.Row(spacing = 5, wrap = True, visible = False, controls = [cus_pre, cus_suf, cus_re, cus_cs])
    #----------#
    hash_cb = ft.Switch(expand = True, label = "[Abc12]添加伪 Hash ID (资源标识符)(由一定位数的字母+数字所构成的字符串)", value = False, on_change = hash_check)
    hash_ws = ft.TextField(width = 150, label = "位数 (3-10)", value = "5", on_blur = ws_check, disabled = True)
    row_hash = ft.Row(spacing = 10, controls = [hash_cb, hash_ws])
    #----------#
    num_pslo = ft.Dropdown(
            label = "数字伪本地化",
            hint_text = "选择数字伪本地化方案, 默认为“无”",
            value = "0",
            options = [
                ft.DropdownOption(key = "0", text = "无"),
                ft.DropdownOption(key = "1", text = "使用①-⑨替代1-9"),
                ft.DropdownOption(key = "2", text = "使用₀-₉或⁰-⁹交叉替换0-9")
            ])
    #----------#
    vowel_tx = ft.Text("重复元音次数(0代表不重复, 1代表双写, 以此类推): ",size=15)
    vowel_cs = ft.TextField(width = 150, label = "次数 (0-10)", value = "0", on_blur = vcs_check)
    row_vow = ft.Row(spacing = 10, controls = [vowel_tx,vowel_cs])
    #----------#
    vis_con_cb = ft.Switch(label = r"翻译后隐藏%s, \n, \r等控制字符", value = False)

    pslo_opt_card = ft.Card(
            content = ft.Container(
                content = ft.Column(
                    [
                        suf_way,
                        cus_ps,
                        row_hash,
                        num_pslo,
                        row_vow,
                        vis_con_cb
                    ]
                ),
                padding = 15
            ),
            elevation = 0.5
        )

    # 外观设置
    opt_look = ft.Row(
            [
                ft.Icon(icon = ft.Icons.PALETTE_OUTLINED),
                ft.Text("外观", size = 22)
            ]
        )
    #----------#
    theme = ft.Dropdown(
            label = "亮暗模式",
            hint_text = "亮暗模式",
            value = "2",
            options=[
                ft.DropdownOption(key = "0", text = "亮色"),
                ft.DropdownOption(key = "1", text = "暗色"),
                ft.DropdownOption(key = "2", text = "跟随系统")
            ],
            on_select = theme_changed)
    #----------#
    sch_text = ft.Text("配色", size = 20)
    scheme = ft.RadioGroup(value = "0", content = ft.Row(controls = [
            ft.Radio(value = "0", label = "蓝色", fill_color = ft.Colors.BLUE_800),
            ft.Radio(value = "1", label = "粉色", fill_color = ft.Colors.PINK_700),
            ft.Radio(value = "2", label = "绿色", fill_color = ft.Colors.GREEN_700),
            ft.Radio(value = "3", label = "巧克力色", fill_color = ft.Colors.BROWN),
            ft.Radio(value = "4", label = "紫色", fill_color = ft.Colors.DEEP_PURPLE)
        ]),
        on_change = sch_changed)
    #----------#
    opacity_text = ft.Text("窗口透明度", size = 20)
    opacity_slider = ft.Slider(min = 50, max = 100, expand = True, divisions = 50, label = "{value}%", on_change = opacity_slider_changed, value = 100)
    opacity_bar = ft.Row(visible = desktop, controls = [opacity_text, ft.Icon(ft.Icons.OPACITY), opacity_slider, ft.Icon(ft.Icons.WATER_DROP)])
    opac_warn_bar = ft.Row(controls = [ft.Icon(ft.Icons.WARNING_AMBER_OUTLINED, color = ft.Colors.AMBER),ft.Text("透明度似乎太低了!", color = ft.Colors.AMBER)], visible = False)

    look_opt_card = ft.Card(
            content = ft.Container(
                content = ft.Column(
                    [
                        theme,
                        sch_text,
                        scheme,
                        opacity_bar,
                        opac_warn_bar
                    ]
                ),
                padding = 15
            ),
            elevation = 0.5
        )

    # 关于内容
    abt = ft.Row(
            [
                ft.Icon(icon = ft.Icons.INFO_OUTLINE),
                ft.Text("关于", size = 22)
            ]
        )
    about = ft.Text(basic_info.about_text, size = 15, selectable = True)
    upd_bar = ft.Row(
        controls = [
            ft.TextButton("更新日志", icon = ft.Icons.UPDATE, on_click = open_upd),
            ft.TextButton("检查更新", icon = ft.Icons.UPLOAD_OUTLINED, on_click = check_for_update)
        ]
    )

    abt_card = ft.Card(
            content = ft.Container(
                content = ft.Column(
                    [
                        about,
                        upd_bar
                    ]
                ),
                padding = 15
            ),
            elevation = 0.5
        )
    set_col = ft.Column(expand = True, horizontal_alignment = ft.CrossAxisAlignment.STRETCH, scroll = ft.ScrollMode.ALWAYS, controls = [opt_pslo, opt_pslo_detail, pslo_opt_card, opt_look, look_opt_card, abt, abt_card])
    set_page = ft.Container(expand = True, content = set_col, visible = False)
    main_area = ft.Column(expand = True, horizontal_alignment = ft.CrossAxisAlignment.STRETCH, controls = [home_page, his_page, collection_page, set_page])

    # 导航栏
    rail = ft.NavigationRail(
        selected_index = 0,
        label_type = ft.NavigationRailLabelType.ALL,
        min_width = 90,
        min_extended_width = 100,
        group_alignment = -1.0,
        destinations = [
            ft.NavigationRailDestination(
                icon = ft.Icons.HOME_OUTLINED, selected_icon = ft.Icons.HOME_ROUNDED, label = "主页"
            ),
            ft.NavigationRailDestination(
                icon = ft.Icons.HISTORY_OUTLINED,
                selected_icon = ft.Icons.HISTORY_ROUNDED,
                label = "历史记录",
            ),
            ft.NavigationRailDestination(
                icon = ft.Icons.ALL_INBOX_OUTLINED,
                selected_icon = ft.Icons.ALL_INBOX,
                label = ft.Text("集合"),
            ),
            ft.NavigationRailDestination(
                icon = ft.Icons.SETTINGS_OUTLINED,
                selected_icon = ft.Icons.SETTINGS,
                label = ft.Text("设置"),
            ),
        ],
        on_change = rail_ctrl,
    )
    main_row = ft.Row(expand = True, vertical_alignment = ft.CrossAxisAlignment.STRETCH, controls = [rail, main_area])
    page.add(titlebar, main_row)
    log.out(0, "Window initialization completed")

if __name__ == "__main__":
    try:
        gil_enabled = sys._is_gil_enabled()
    except AttributeError:
        gil_enabled = True

    if gil_enabled == False:
        log.out(3, "Free-threaded build of Python detected, stability cannot be guaranteed!")

    ft.run(main)
