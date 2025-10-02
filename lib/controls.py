import flet
from flet import *
from flet import Icons
from lib import log # 日志输出库

# 预备输出
log.out(0, "Advanced Controls Module ready...")

# 窗口顶栏, 基于Fleter库制作, MIT协议
def CLOSE_ID(page: flet.Page):
    page.window.close()
    page.close_in_app_web_view()

def MAXIMIZE_ID(page: flet.Page):
    if page.window.maximized:
        page.window.maximized = False
    elif not page.window.maximized:
        page.window.maximized = True
    page.update()

def MINIMIZE_ID(page: flet.Page):
    page.window.minimized = True
    page.update()

class CloseButton(IconButton):
    __name__ = "controls.CloseButton"

    def __init__(self,
                 page: flet.Page,
                 icon = Icons.CLOSE_ROUNDED,
                 on_click=None,
                 ):
        super(CloseButton, self).__init__(icon = icon)

        self._page = page

        if on_click is None:
            self.on_click = lambda _: self.close()

    def close(self):
        CLOSE_ID(self._page)


class MaximizeButton(IconButton):
    __name__ = "controls.MaximizeButton"

    def __init__(self,
                 page: flet.Page,
                 icon = Icons.ZOOM_OUT_MAP_ROUNDED,
                 icon_max = Icons.ZOOM_IN_MAP_ROUNDED,
                 on_click = None,
                 ):
        super(MaximizeButton, self).__init__(icon = icon, icon_size = 20)

        self._page = page

        self._icon = icon
        self._icon_max = icon_max

        if on_click is None:
            self.on_click = lambda _: self.maximize()

    def maximize(self):
        if self._page.window.maximized:
            self.icon = self._icon
        elif not self._page.window.maximized:
            self.icon = self._icon_max
        MAXIMIZE_ID(self._page)
        self._page.update()


class MinimizeButton(IconButton):
    __name__ = "controls.MinimizeButton"

    def __init__(self,
                 page: flet.Page,
                 icon = Icons.MINIMIZE_ROUNDED,
                 on_click = None,
                 ):
        super(MinimizeButton, self).__init__(icon = icon)

        self._page = page

        if on_click is None:
            self.on_click = lambda _: self.minimize()

    def minimize(self):
        self._page.window.minimized = True
        MINIMIZE_ID(self._page)
        self._page.update()