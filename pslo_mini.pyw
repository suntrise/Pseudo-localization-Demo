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
        page.result.value = pslo_work.pslo(page.pstype.value, "enxa", 0, 0, 0, False, 0)
        page.update()
         
    # 复制文本
    def copy_text(e):
        pyperclip.copy(page.result.value)
        print("\033[0;32m[DONE] Added to clipboard\033[0m")
        page.snack_bar = ft.SnackBar(ft.Text(f"已复制")) # 提示栏
        page.snack_bar.open = True
        page.update()
        print("\033[0;34m[INFO] Snack bar pop-up(CP)\033[0m")

    # 用户界面
    # 基本内容定义
    page.window_left = 200
    page.window_top = 100
    page.window_height = 275
    page.window_width = 300  
    page.window_opacity = 0.9
    page.window_resizable = False
    page.theme = ft.Theme(
         font_family = "Microsoft Yahei",
         color_scheme_seed = ft.colors.BLUE
         )

    # 主页区
    titlebar = fleter.HeaderBar(page, title = "₽ŠĹȮ ❤️ " + basic_info.ver, title_align = "left")
    titlebar.controls.insert(1, fleter.SwitchThemeButton(page, has_system=False))
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size = 13, multiline = False, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 13, multiline = False, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
        "伪本地化!",
        icon = ft.icons.TRANSLATE_OUTLINED,
        on_click = pslo     
        )
    copy_btn = ft.IconButton(
                icon = ft.icons.COPY_OUTLINED,
                on_click = copy_text
            )
    row = ft.Row(controls=[pslo_btn, copy_btn])
    page.add(titlebar, page.pstype, page.result, row)
    print("\033[0;34m[INFO] Window initialization completed\033[0m")

ft.app(target = main)
