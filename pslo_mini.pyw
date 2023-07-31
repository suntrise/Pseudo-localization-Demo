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
        if page.window_always_on_top == False:
            page.window_always_on_top = True
            ontop_btn.icon = ft.icons.PUSH_PIN_ROUNDED
            log.out(1, "Set always on top")
            page.update()
        elif page.window_always_on_top == True:
            page.window_always_on_top = False
            ontop_btn.icon = ft.icons.PUSH_PIN_OUTLINED
            log.out(1, "Cancel always on top")
            page.update()

    def switch_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            theme_switch_btn.icon = ft.icons.LIGHT_MODE_OUTLINED
            page.theme_mode = ft.ThemeMode.LIGHT
        elif page.theme_mode == ft.ThemeMode.LIGHT:
            theme_switch_btn.icon = ft.icons.DARK_MODE_OUTLINED
            page.theme_mode = ft.ThemeMode.DARK
        page.update()


    # 用户界面
    # 基本内容定义
    page.window_left = 200
    page.window_top = 100
    page.window_height = 263
    page.window_width = 400  
    page.window_opacity = 0.9
    page.window_resizable = False
    page.window_title_bar_hidden = True
    page.theme = ft.Theme(
        font_family = "Microsoft Yahei",
        color_scheme_seed = ft.colors.BLUE
    )
    page.theme_mode = ft.ThemeMode.LIGHT

    # 主页区
    # 窗口区
    title_text = ft.Container(ft.Text("伪本地化演示Mini", size = 18))
    title_icon = ft.Container(ft.Icon(ft.icons.LANGUAGE_OUTLINED, size = 18), padding = 5)
    ontop_btn = ft.IconButton(icon = ft.icons.PUSH_PIN_OUTLINED, on_click = always_on_top, tooltip = "置顶") 
    theme_switch_btn = ft.IconButton(icon = ft.icons.LIGHT_MODE_OUTLINED, on_click = switch_theme, tooltip = "明暗")
    min_btn = controls.MinimizeButton(page, icon = ft.icons.HORIZONTAL_RULE_ROUNDED) 
    close_btn = controls.CloseButton(page)
    titlebar = ft.WindowDragArea(ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        controls = [
            ft.Row(spacing = 1, controls = [title_icon, title_text]),
            ft.Row(spacing = 1,controls = [ontop_btn, theme_switch_btn, min_btn, close_btn])
        ]))  
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size = 15, multiline = False, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = False, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledTonalButton(
            "伪本地化!",
            icon = ft.icons.TRANSLATE_OUTLINED,
            style = ft.ButtonStyle(
                shape = ft.RoundedRectangleBorder(radius = 5),
            ),
            on_click = pslo     
        )
    copy_btn = ft.IconButton(
                icon = ft.icons.COPY_OUTLINED,
                on_click = copy_text
            )
    copy_notice = ft.Row(
        controls = [
            ft.Icon(ft.icons.DONE, color = ft.colors.GREEN_600),
            ft.Text("已复制", color = ft.colors.GREEN_600)
        ],
        visible = False
    )
    btns = ft.Row(controls = [pslo_btn, copy_btn])
    row = ft.Row(controls = [btns, copy_notice, ft.Text(basic_info.ver, size = 15, color = ft.colors.GREY)], alignment = ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(titlebar, page.pstype, page.result, row)
    log.out(0, "Window initialization completed")

ft.app(target = main)
