import flet as ft
import sys
import pyperclip
import fleter
from lib import pslo_work
from lib import basic_info

# 基础信息位于lib/basic_info.py

print('\033[0;34m[INFO] Python version: {}\033[0m'.format(sys.version))
print("\033[0;34m[INFO] PSLO version: " + basic_info.ver + "\033[0m")
print("\033[0;34m[INFO] You are using PSLO Mini\033[0m")

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
        print("\033[0;32m[DONE] Added to clipboard\033[0m")
        page.snack_bar = ft.SnackBar(ft.Text(f"已复制")) # 提示栏
        page.snack_bar.open = True
        page.update()
        print("\033[0;34m[INFO] Snack bar pop-up(CP)\033[0m")

    # 置顶
    def always_on_top(e):
        if page.window_always_on_top == False:
            page.window_always_on_top = True
            ontop_btn.icon = ft.icons.PUSH_PIN_ROUNDED
            print("\033[0;32m[DONE] Set always on top\033[0m")
            print("\033[0;32m[DONE] Snack Bar pop-up(AOT)\033[0m")
            page.update()
        elif page.window_always_on_top == True:
            page.window_always_on_top = False
            ontop_btn.icon = ft.icons.PUSH_PIN_OUTLINED
            print("\033[0;32m[DONE] Cancel always on top\033[0m")
            print("\033[0;32m[DONE] Snack Bar pop-up(ATX)\033[0m")
            page.update()

    # 用户界面
    # 基本内容定义
    page.window_left = 200
    page.window_top = 100
    page.window_height = 300
    page.window_width = 400  
    page.window_opacity = 0.9
    page.window_resizable = False
    page.theme = ft.Theme(
         font_family = "Microsoft Yahei",
         color_scheme_seed = ft.colors.BLUE
         )

    # 主页区
    titlebar = fleter.HeaderBar(page, title = "伪本地化演示 mini",title_align = "left")
    # titlebar._title_area = ft.Container(padding = 5)
    titlebar.controls.insert(1, fleter.SwitchThemeButton(page, light_icon = ft.icons.LIGHT_MODE, dark_icon = ft.icons.DARK_MODE, has_system = False))    
    ontop_btn = ft.IconButton(icon = ft.icons.PUSH_PIN_OUTLINED, on_click = always_on_top) 
    titlebar.controls.insert(2,ontop_btn)
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size = 15, multiline = False, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = False, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
            "伪本地化!",
            icon = ft.icons.TRANSLATE_OUTLINED,
            on_click = pslo     
        )
    copy_btn = ft.IconButton(
                icon = ft.icons.COPY_OUTLINED,
                on_click = copy_text
            )
    btns = ft.Row(controls=[pslo_btn, copy_btn])
    row = ft.Row(controls=[btns, ft.Text(basic_info.ver, size = 15, color = ft.colors.GREY)], alignment = ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(titlebar, page.pstype, page.result, row)
    print("\033[0;34m[INFO] Window initialization completed\033[0m")

ft.app(target = main)
