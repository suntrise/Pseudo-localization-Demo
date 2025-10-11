import flet as ft
import sys
import pyperclip
import time
from lib import log
from lib import pslo_work
from lib import controls
from lib import basic_info

# 基础信息位于lib/basic_info.py

log.out(0, "Python version: " + sys.version)
log.out(0, "PSLO version: " + basic_info.ver)
log.out(0, "You are using PSLO Mini")

# 主程序
def main(page: ft.Page):

    # 原pslo函数已迁移至lib/pslo_work.py

    # 伪本地化
    def pslo(e):
        global pshis
        page.result.value = pslo_work.pslo(page.pstype.value, "enxa", 0, 0, 0, "", "", "", 0, False, 0, False)
        page.update()
         
    # 复制文本
    def copy_text(e):
        pyperclip.copy(page.result.value)
        log.out(1, "Added to clipboard")
        copy_notice.visible = True
        log.out(1, "Copy notice visable is True")
        page.update()
        time.sleep(2)
        copy_notice.visible = False
        log.out(1, "Copy notice visable is False")
        page.update()

    # 置顶
    def always_on_top(e):
        if page.window.always_on_top == False:
            page.window.always_on_top = True
            ontop_btn.icon = ft.Icons.PUSH_PIN_ROUNDED
            log.out(1, "Set always on top")
            page.update()
        elif page.window.always_on_top == True:
            page.window.always_on_top = False
            ontop_btn.icon = ft.Icons.PUSH_PIN_OUTLINED
            log.out(1, "Cancel always on top")
            page.update()

    def switch_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            theme_switch_btn.icon = ft.Icons.LIGHT_MODE_OUTLINED
            page.theme_mode = ft.ThemeMode.LIGHT
        elif page.theme_mode == ft.ThemeMode.LIGHT:
            theme_switch_btn.icon = ft.Icons.DARK_MODE_OUTLINED
            page.theme_mode = ft.ThemeMode.DARK
        page.update()


    # 用户界面
    # 基本内容定义
    page.window.left = 200
    page.window.top = 100
    page.window.height = 263
    page.window.width = 400  
    page.window.opacity = 0.9
    page.window.resizable = False
    page.window.title_bar_hidden = True
    page.theme = ft.Theme(
        font_family = "Microsoft Yahei",
        color_scheme_seed = ft.Colors.BLUE
    )
    page.theme_mode = ft.ThemeMode.LIGHT

    # 主页区
    # 窗口区
    title_text = ft.Container(ft.Text("伪本地化演示Mini", size = 18))
    title_icon = ft.Container(ft.Icon(ft.Icons.LANGUAGE_OUTLINED, size = 18), padding = 5)
    ontop_btn = ft.IconButton(icon = ft.Icons.PUSH_PIN_OUTLINED, on_click = always_on_top, tooltip = "置顶") 
    theme_switch_btn = ft.IconButton(icon = ft.Icons.LIGHT_MODE_OUTLINED, on_click = switch_theme, tooltip = "明暗")
    if sys.platform != 'darwin':
        min_btn = controls.MinimizeButton(page, icon = ft.Icons.HORIZONTAL_RULE_ROUNDED) 
        close_btn = controls.CloseButton(page)
        titlebar_controls = [ontop_btn, theme_switch_btn, min_btn, close_btn]
    else:
        titlebar_controls = [ontop_btn, theme_switch_btn]
    titlebar = ft.WindowDragArea(ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        controls = [
            ft.Row(spacing = 1, controls = [title_icon, title_text]),
            ft.Row(spacing = 1,controls = titlebar_controls)
        ]))  
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size = 15, multiline = False, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = False, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledTonalButton(
            "伪本地化!",
            icon = ft.Icons.TRANSLATE_OUTLINED,
            style = ft.ButtonStyle(
                shape = ft.RoundedRectangleBorder(radius = 5),
            ),
            on_click = pslo     
        )
    copy_btn = ft.IconButton(
                icon = ft.Icons.COPY_OUTLINED,
                on_click = copy_text
            )
    copy_notice = ft.Row(
        controls = [
            ft.Icon(ft.Icons.DONE, color = ft.Colors.GREEN_600),
            ft.Text("已复制", color = ft.Colors.GREEN_600)
        ],
        visible = False
    )
    btns = ft.Row(controls = [pslo_btn, copy_btn])
    row = ft.Row(controls = [btns, copy_notice, ft.Text(basic_info.ver, size = 15, color = ft.Colors.GREY)], alignment = ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(titlebar, page.pstype, page.result, row)
    log.out(0, "Window initialization completed")

if __name__ == "__main__":
    try:
        gil_enabled = sys._is_gil_enabled()     
    except AttributeError:
        gil_enabled = True
    
    if gil_enabled == False:
        log.out(3, "Free-threaded build of Python detected, stability cannot be guaranteed!")
    
    ft.app(target = main)