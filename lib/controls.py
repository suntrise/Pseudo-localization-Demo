"""Flet 1.0 native window controls."""

import flet as ft


@ft.control
class CloseButton(ft.IconButton):
    def init(self):
        self.icon = self.icon or ft.Icons.CLOSE_ROUNDED
        self.on_click = self.on_click or self.close

    async def close(self, e):
        await self.page.window.close()


@ft.control
class MaximizeButton(ft.IconButton):
    icon_max: ft.IconData = ft.Icons.ZOOM_IN_MAP_ROUNDED

    def init(self):
        self.icon = self.icon or ft.Icons.ZOOM_OUT_MAP_ROUNDED
        self.icon_size = 20
        self._restore_icon = self.icon
        self.on_click = self.on_click or self.maximize

    def maximize(self, e):
        window = self.page.window
        window.maximized = not window.maximized
        self.icon = self.icon_max if window.maximized else self._restore_icon
        self.page.update()


@ft.control
class MinimizeButton(ft.IconButton):
    def init(self):
        self.icon = self.icon or ft.Icons.MINIMIZE_ROUNDED
        self.on_click = self.on_click or self.minimize

    def minimize(self, e):
        self.page.window.minimized = True
        self.page.update()
