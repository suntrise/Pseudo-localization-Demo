import flet as ft # 界面库
import fleter
import pyperclip # 复制库
import webbrowser # 浏览器链接库
import sys # 系统库
import datetime # 日期时间库
from lib import pslo_work # 工作模块
from lib import update # 更新模块
from lib import basic_info # 基础信息
# from lib import config_li # 写入配置库, 尚未完成

# 基础信息位于lib/basic_info.py

# 变量初始化
pshis = ""
print('\033[0;34m[INFO] Python version: {}\033[0m'.format(sys.version))
print("\033[0;34m[INFO] PSLO version: " + basic_info.ver + "\033[0m")

# 主程序
# 主程序
def main(page: ft.Page):
    # 字符相隔位数是否数字确定
    def ccs_check(e):
        if cus_cs.value.isdigit() == False:
            cus_cs.value = 7; 
            print("\033[0;34m[INFO] Set the CUS value to 7\033[0m")
        page.update()

    # 是否显示前后缀配置栏
    def psf_check(e):
        if suf_way.value == "3":
            cus_ps.visible = True
            print("\033[0;34m[INFO] CUS Toolbar visible is true\033[0m")
        else:
            cus_ps.visible = False
            print("\033[0;34m[INFO] CUS Toolbar visible is false\033[0m")
        page.update()
    
    # 原pslo函数已迁移至lib/pslo_work.py

    # 伪本地化&内容获取
    def pslo(e):
        global pshis
        page.result.value = pslo_work.pslo(page.pstype.value, xab.value, num_pslo.value, vowel_cs.value, suf_way.value, cus_pre.value, cus_suf.value, cus_re.value, cus_cs.value, hash_cb.value, hash_ws.value, vis_con_cb.value)
        pshis += page.pstype.value + " → " + page.result.value +" | " + datetime.datetime.now().strftime('%H:%M:%S') + "\n" # 添加到历史记录
        history.value = pshis
        print("\033[0;32m[DONE] Added content to history\033[0m")
        page.update()

    # 复制文本
    def copy_text(e):
        pyperclip.copy(page.result.value)
        print("\033[0;32m[DONE] Added to clipboard\033[0m")
        page.snack_bar = ft.SnackBar(ft.Text(f"已复制")) # 提示栏
        page.snack_bar.open = True
        page.update()
        print("\033[0;34m[INFO] Snack bar pop-up(CP)\033[0m")

    # 复制历史记录
    def copy_history(e):
        pyperclip.copy(history.value)
        print("\033[0;32m[DONE] Added history to clipboard\033[0m")
        page.snack_bar = ft.SnackBar(ft.Text(f"已复制历史记录")) # 提示栏
        page.snack_bar.open = True
        page.update()
        print("\033[0;34m[INFO] Snack bar pop-up(CPH)\033[0m")
        
    # 导入文件
    def ps_files(e: ft.FilePickerResultEvent):
        psfile = ", ".join(map(lambda f: f.path, e.files)) if e.files else "ERR"
        if psfile != "ERR":
            page.snack_bar = ft.SnackBar(ft.Text("检测到文件: " + psfile)) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(UL)\033[0m")
            with open(psfile, encoding = 'utf-8') as psf:
                page.pstype.value = psf.read()
                print("\033[0;32m[DONE] TXT:" + psf.read() + "\033[0m")
                pslo(e) 
        else:
            page.snack_bar = ft.SnackBar(ft.Text("未检测到文件")) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(UF)\033[0m")
        page.update()

    # 导出文件
    def sv_files(e: ft.FilePickerResultEvent):
        svfile = e.path if e.path else "ERR"
        if sv_files != "ERR":
            page.snack_bar = ft.SnackBar(ft.Text("已保存至: " + svfile)) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(SV)\033[0m")
            with open(svfile, "a", encoding = 'utf-8') as svf:
                svf.write(page.result.value)
                print("\033[0;32m[DONE] File saved:" + str(svfile) + "\033[0m")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("发生错误, 不是合法的路径")) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(SVE)\033[0m")
        page.update()

    # 导出历史记录
    def sv_his(e: ft.FilePickerResultEvent):
        svhis = e.path if e.path else "ERR"
        if svhis != "ERR":
            page.snack_bar = ft.SnackBar(ft.Text("已保存至: " + svhis)) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(SVH)\033[0m")
            with open(svhis, "a", encoding = 'utf-8') as svh:
                svh.write(history.value)
                print("\033[0;32m[DONE] File saved:" + str(svhis) + "\033[0m")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("发生错误, 不是合法的路径")) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(SHE)\033[0m")
        page.update()    

    # 清除历史记录
    def clear_his(e):
        close_chq(e)
        pshis = ""
        history.value = "无记录"
        print("\033[0;32m[DONE] History is cleared\033[0m")
        page.snack_bar = ft.SnackBar(ft.Text(f"已清空")) # 提示栏
        page.snack_bar.open = True
        page.update()
        print("\033[0;34m[INFO] Snack bar pop-up(CH)\033[0m")
    
    # Hash输入框解禁
    def hash_check(e):
        if hash_cb.value == True:
            hash_ws.disabled = False
            print("\033[0;34m[INFO] Hash ID text field is enable\033[0m")
        else:
            hash_ws.disabled = True
            print("\033[0;34m[INFO] Hash ID text field is disabled\033[0m")
        page.update()

    # Hash数值确认
    def ws_check(e):
        ws = hash_ws.value
        if str(ws).isdigit() == False:
            hash_ws.value = 5  
            print("\033[0;34m[INFO] Set the Hash ID text field value to 5\033[0m")
        elif int(ws) < 3:
            hash_ws.value = 3
            print("\033[0;34m[INFO] The value is too small, has set the Hash ID text field value to 3\033[0m")
        elif int(ws) > 10:
            hash_ws.value = 10 
            print("\033[0;34m[INFO] The value is too big, has set the Hash ID text field value to 10\033[0m")
        page.update()

    # 元音重复次数检测
    def vcs_check(e):
        vcs = vowel_cs.value
        if str(vcs).isdigit() == False:
            vowel_cs.value = 0
            print("\033[0;34m[INFO] Set the Vowel repetition text field value to 0\033[0m")
        elif int(vcs) < 0:
            vowel_cs.value = 0
            print("\033[0;34m[INFO] The value is too small, has set the Vowel repetition text field value to 0\033[0m")
        elif int(vcs) > 10:
            vowel_cs.value = 10 
            print("\033[0;34m[INFO] The value is too big, has set the Vowel repetition text field value to 10\033[0m")
        page.update()

    # 明暗切换
    def theme_changed(e):
        if theme.value == "0":
            page.theme_mode = (
                ft.ThemeMode.LIGHT # 亮色
            )
            print("\033[0;32m[DONE] Switch to LIGHT\033[0m")
        if theme.value == "1":
            page.theme_mode = (
                ft.ThemeMode.DARK # 暗黑
            )
            print("\033[0;32m[DONE] Switch to DARK\033[0m")
        if theme.value == "2":
            page.theme_mode = (
                ft.ThemeMode.SYSTEM # 系统
            )
            print("\033[0;32m[DONE] Switch to SYSTEM\033[0m")
        page.update()

    # 色彩选择
    def sch_changed(e):
        sch = int(scheme.value)
        if sch == 0:
            page.theme=ft.Theme(font_family = "Microsoft Yahei",
                            color_scheme_seed = ft.colors.BLUE) # 蓝色
            print("\033[0;32m[DONE] Switch to color BLUE\033[0m")
        if sch == 1:
            page.theme=ft.Theme(font_family = "Microsoft Yahei",
                            color_scheme_seed = ft.colors.PINK) # 粉色
            print("\033[0;32m[DONE] Switch to color PINK\033[0m")
        if sch == 2:
            page.theme=ft.Theme(font_family = "Microsoft Yahei",
                            color_scheme_seed = ft.colors.GREEN) # 绿色
            print("\033[0;32m[DONE] Switch to color GREEN\033[0m")
        if sch == 3:
            page.theme=ft.Theme(font_family = "Microsoft Yahei",
                            color_scheme_seed = ft.colors.BROWN) # 巧克力色
            print("\033[0;32m[DONE] Switch to color BROWN\033[0m")
        if sch == 4:
            page.theme=ft.Theme(font_family = "Microsoft Yahei",
                            color_scheme_seed = ft.colors.DEEP_PURPLE_100) # 紫色
            print("\033[0;32m[DONE] Switch to color DEEP_PURPLE\033[0m")
        page.update()

    # 透明度设置
    def opacity_slider_changed(e):
        opac_value = page.opacity_slider.value / 100
        page.window_opacity = opac_value
        print("\033[0;32m[DONE] Window opacity: " + str(page.window_opacity) + "\033[0m")
        page.update()
    
    # 打开网页版
    def open_with_browser(e):
        webbrowser.open_new("https://suntrise.github.io/pseudo/")
        print("\033[0;32m[DONE] Website open (OIB)\033[0m")

    # 打开项目仓库
    def open_project_repo(e):
        webbrowser.open_new("https://github.com/suntrise/Pseudo-localization-Demo")
        print("\033[0;32m[DONE] Website open (OPR)\033[0m")

    # 打开“什么是伪本地化”窗口
    def open_what(e):
        page.dialog = what_dlg
        what_dlg.open = True
        print("\033[0;32m[DONE] Dialog open(WHT)\033[0m")
        page.update()  
    
    # 关闭“什么是伪本地化”窗口
    def close_what(e):
        what_dlg.open = False
        print("\033[0;32m[DONE] Dialog close(WHT)\033[0m")
        page.update()

    # 打开“确定清除历史记录”窗口
    def open_chq(e):
        page.dialog = chq_dlg
        chq_dlg.open = True
        print("\033[0;32m[DONE] Dialog open(CHQ)\033[0m")
        page.update()  

    # 关闭“确定清除历史记录”窗口
    def close_chq(e):
        chq_dlg.open = False
        print("\033[0;32m[DONE] Dialog close(CHQ)\033[0m")
        page.update()

    # 打开“更新日志”窗口
    def open_upd(e):
        page.dialog = upd_dlg
        upd_dlg.open = True
        print("\033[0;32m[DONE] Dialog open(UPH)\033[0m")
        page.update() 

    # 原check_for_update函数已迁移至lib/update.py
    
    # 检查更新
    def check_for_update(e):
        # 关闭“发现更新”窗口
        def close_find_upd_dlg(e):
            find_upd_dlg.open = False
            page.update()
            print("\033[0;32m[DONE] Dialog close(UPD)\033[0m")
        content = update.update(basic_info.ver)
        if content == "ERR":
            page.snack_bar = ft.SnackBar(ft.Text(f"检查更新超时, 请检查网络连接")) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;32m[DONE] Snack Bar pop-up(CUF)\033[0m")
        elif content == "NUL":
            page.snack_bar = ft.SnackBar(ft.Text(f"你正在使用最新版本")) # 提示栏
            page.snack_bar.open = True
            print("\033[0;32m[DONE] Snack Bar pop-up(VLT)\033[0m")
            page.update()
        else:
            download_url = update.get_link()
            # 定义“发现更新”窗口
            find_upd_dlg = ft.AlertDialog(
                title = ft.Text("发现更新"), on_dismiss = lambda e: print("\033[0;34m[INFO] Dialog dismissed(UPD)\033[0m"),
                content = ft.Markdown(content, selectable = True),
                actions = [
                    ft.FilledButton("更新", icon = ft.icons.UPLOAD_OUTLINED, url = download_url),
                    ft.TextButton("取消", icon = ft.icons.CLOSE_OUTLINED, on_click = close_find_upd_dlg)
                ],
            )
            page.dialog = find_upd_dlg # 打开“发现更新”窗口
            find_upd_dlg.open = True
            page.update()  
            print("\033[0;32m[DONE] Dialog open(UPD)\033[0m")

    #检测窗口大小
    def page_resize(e):
        his_card.width = page.window_width
        home_page.height = page.window_height-90
        home_page.width = page.window_width-120
        his_page.height = page.window_height-90
        his_page.width = page.window_width-120
        set_page.height = page.window_height-90
        set_page.width = page.window_width-120
        main_area.width = page.window_width-120
        main_row.width = page.window_width
        page.update()
        print("New page size:",round(page.window_height),round(page.window_width))

    # 置顶
    def always_on_top(e):
        if page.window_always_on_top == False:
            page.window_always_on_top = True
            ontop_btn.icon = ft.icons.PUSH_PIN_ROUNDED
            print("\033[0;32m[DONE] Set always on top\033[0m")
            page.snack_bar = ft.SnackBar(ft.Text(f"已置顶")) # 提示栏
            page.snack_bar.open = True
            print("\033[0;32m[DONE] Snack Bar pop-up(AOT)\033[0m")
            page.update()
        elif page.window_always_on_top == True:
            page.window_always_on_top = False
            ontop_btn.icon = ft.icons.PUSH_PIN_OUTLINED
            print("\033[0;32m[DONE] Cancel always on top\033[0m")
            page.snack_bar = ft.SnackBar(ft.Text(f"已取消置顶")) # 提示栏
            page.snack_bar.open = True
            print("\033[0;32m[DONE] Snack Bar pop-up(ATX)\033[0m")
            page.update()

    #小窗模式
    def mini_mode(e):
        if rail.visible == True:
            mini_btn.icon = ft.icons.VERTICAL_ALIGN_TOP_ROUNDED
            mini_btn.tooltip = "恢复小窗"
            page.window_height = 350
            page.window_width = 500
            page.window_resizable = False
            max_btn.visible = False
            page.pstype.max_lines = 1
            page.result.max_lines = 1
            rail.selected_index=0
            rail_ctrl(e)
            rail.visible = False
        elif rail.visible == False:
            mini_btn.icon = ft.icons.PHOTO_SIZE_SELECT_SMALL_ROUNDED
            mini_btn.tooltip = "小窗模式"
            page.window_height = 600
            page.window_width = 900        
            page.window_resizable = True
            max_btn.visible = True
            page.pstype.max_lines = 5
            page.result.max_lines = 5
            rail.visible = True
        page.update()

    #导航栏控制
    def rail_ctrl(e):
        if rail.selected_index == 0:
            home_page.visible = True
            his_page.visible = False
            set_page.visible = False       
        elif rail.selected_index == 1:
            home_page.visible = False
            his_page.visible = True
            set_page.visible = False
        elif rail.selected_index == 2:
            home_page.visible = False
            his_page.visible = False
            set_page.visible = True
        print("Navigate to: ",rail.selected_index)
        page.update()

    # “什么是伪本地化”窗口定义
    what_dlg = ft.AlertDialog(
        title = ft.Text("什么是伪本地化?"), on_dismiss = lambda e: print("\033[0;34m[INFO] Dialog dismissed(WHT)\033[0m"),
        content = ft.Markdown(basic_info.what_text, selectable = True),
        actions = [
            ft.TextButton("我知道啦", icon = ft.icons.DONE, on_click = close_what)      
        ],
        actions_alignment = ft.MainAxisAlignment.END
    ) 

    # “确定清除历史记录”窗口定义
    chq_dlg = ft.AlertDialog(
        title = ft.Text("确定删除历史记录?"), on_dismiss = lambda e: print("\033[0;34m[INFO] Dialog dismissed(CHQ)\033[0m"),
        content = ft.Text("确定删除所有历史记录,?\n该操作不可逆!"),
        actions = [
            ft.ElevatedButton("确定", icon = ft.icons.DONE, on_click = clear_his, bgcolor = ft.colors.RED, color=ft.colors.WHITE, elevation = 0),
            ft.FilledTonalButton("取消", icon = ft.icons.CLOSE, on_click = close_chq)      
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
            width = page.window_width,
        ),
        on_dismiss = lambda e: print("\033[0;34m[INFO] Dialog dismissed(UPH)\033[0m")
    )
         
   
    # 用户界面
    # 基本内容定义
    page.window_left = 200
    page.window_top = 100
    page.window_height = 600
    page.window_width = 900
    page.window_min_height = 350
    page.window_min_width = 500
    page.window_title_bar_hidden = True
    page.theme = ft.Theme(
         font_family = "Microsoft Yahei",
         color_scheme_seed = ft.colors.BLUE
         )
    page.on_resize = page_resize

    # 主页区
    title_text = ft.Container(ft.Text(basic_info.title,size=20))
    theme_btn = fleter.SwitchThemeButton(page, light_icon = ft.icons.LIGHT_MODE, dark_icon = ft.icons.DARK_MODE, has_system = False),
    ontop_btn = ft.IconButton(icon = ft.icons.PUSH_PIN_OUTLINED, on_click = always_on_top) 
    mini_btn = ft.IconButton(icon = ft.icons.PHOTO_SIZE_SELECT_SMALL_ROUNDED, tooltip = "小窗模式", on_click = mini_mode)
    min_btn = fleter.MinimizeButton(page,icon=ft.icons.HORIZONTAL_RULE_ROUNDED) 
    max_btn = fleter.MaximizeButton(page,icon=ft.icons.SQUARE_OUTLINED)  
    close_btn = fleter.CloseButton(page)
    titlebar = ft.WindowDragArea(ft.Row(
        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
        title_text,
        ft.Row(spacing=1,controls=[ontop_btn,mini_btn,min_btn,max_btn,close_btn])
        ]))  
    xab = ft.RadioGroup(value = "enxa",content=ft.Row([
    ft.Radio(value = "enxa", label = "en-XA (ab→ǻƀ)"),
    ft.Radio(value = "enxb", label = "en-XB (ab→ba)")]))
    XABrow = ft.Row(spacing = 1, controls = [ft.Text("伪本地化方式:",size=15),xab])
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size =15, multiline = True, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = True, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
        "进行伪本地化!",
        icon = ft.icons.TRANSLATE_OUTLINED,
        tooltip = "将您所填写的内容伪本地化, 每次生成结果都会不一样哦",
        on_click = pslo     
        )
    copy_btn = ft.IconButton(
        icon = ft.icons.COPY,
        tooltip = "将生成内容添加到设备剪切板",
        on_click = copy_text     
        )
    # 导入导出文件   
    pick_files_dialog = ft.FilePicker(on_result = ps_files)
    save_files_dialog = ft.FilePicker(on_result = sv_files)
    page.overlay.append(pick_files_dialog)
    page.overlay.append(save_files_dialog)
    lsfile = ft.PopupMenuButton(
        icon = ft.icons.EXPAND_MORE_OUTLINED,
        tooltip = "展开查看更多选项",
        items = [
            ft.PopupMenuItem(                
                content = ft.Row(
                [
                    ft.Icon(ft.icons.UPLOAD_FILE_OUTLINED),
                    ft.Text("导入"),
                ]),
               on_click = lambda _: pick_files_dialog.pick_files(allowed_extensions = ["txt"])
            ),
            ft.PopupMenuItem(                
                content = ft.Row(
                [
                    ft.Icon(ft.icons.SAVE_OUTLINED),
                    ft.Text("保存"),
                ]),
               on_click = lambda _: save_files_dialog.save_file(allowed_extensions = ["txt"])
            )
        ]
    )
    pslo_row = ft.Row(spacing = 10, controls = [pslo_btn, copy_btn, lsfile])
    home_page = ft.Column(
        width=page.window_width-120,
        controls=[XABrow, page.pstype, page.result,pslo_row])
    history = ft.Text("无记录", size = 18, selectable = True)    
    his_card = ft.Card(
            content = ft.Container(
                content = ft.Column(
                    [
                        history
                    ]
                ),
                width=page.window_width,
                padding = 10,
            ),elevation = 0.5
        )
    save_his_dialog = ft.FilePicker(on_result = sv_his)
    his_title = ft.Row(controls = [
        ft.Icon(
            ft.icons.LIST_ALT_OUTLINED
        ),
        ft.Text(
            "历史记录:",
            size = 20
        )])
    his_opts = ft.Row(spacing = 5,controls=[
        save_his_dialog,
        ft.TextButton(
            "复制全部",
            icon = ft.icons.COPY_OUTLINED,
            on_click = copy_history
        ),
        ft.TextButton(
            "导出记录",
            icon = ft.icons.SAVE_OUTLINED,
            on_click = lambda _: save_his_dialog.save_file(allowed_extensions = ["txt"])
        ),
        ft.TextButton(
            "清空",
            icon = ft.icons.DELETE_FOREVER_OUTLINED,
            on_click = open_chq
        )
    ])
    his_bar = ft.Row(alignment = ft.MainAxisAlignment.SPACE_BETWEEN,controls = [
        his_title,
        his_opts
    ])
    his_col = ft.Column(
                width=page.window_width-120,
                scroll=ft.ScrollMode.ALWAYS,
                        controls=[
                        his_bar,
                        his_card
        ])
    his_page = ft.Container(
        content = his_col, 
        visible=False)
        # 设置区
    # 伪本地化设置
    opt_pslo = ft.Row(
            [
                ft.Icon(name = ft.icons.TRANSLATE_OUTLINED),
                ft.Text("伪本地化", size = 22)
            ]
        )
    opt_pslo_detail = ft.Text("(部分选项仅适用于 en-XA)", size=15) 
    #----------#
    suf_way = ft.Dropdown(
            label = "前后缀",
            value = 0,
            hint_text = "选择前后缀方案，默认为“不添加前后缀”",
            options=[
                ft.dropdown.Option(key = 0, text = "不添加前后缀"),
                ft.dropdown.Option(key = 1, text = "[中括号+感叹号括起来 (微软式伪本地化)!!!]"),
                ft.dropdown.Option(key = 2, text = "[中括号+在语段后添加英文基数词 (安卓式伪本地化) one two three]"),
                ft.dropdown.Option(key = 3, text = "自定义前后缀")
           ], on_change = psf_check) 
    cus_pre = ft.TextField(width = 80, label = "前缀", value = "[")
    cus_suf = ft.TextField(width = 80, label = "后缀", value = "]")
    cus_re = ft.TextField(label = "在语段后重复添加……")
    cus_cs = ft.TextField(width = 230, label = "每隔多少个字符重复一次：", value = 7, on_blur = ccs_check)
    cus_ps = ft.Row(spacing = 5, visible = False, controls = [cus_pre, cus_suf, cus_re, cus_cs])
    #----------#
    hash_cb = ft.Switch(label = "[Abc12]添加伪 Hash ID (资源标识符)\n(由一定位数的字母+数字所构成的字符串)", value = False, on_change = hash_check)
    hash_ws = ft.TextField(width = 150, label = "位数 (3-10)", value = 5, on_blur = ws_check, disabled = True) 
    row_hash = ft.Row(spacing = 10, controls = [hash_cb, hash_ws])
    #----------#
    num_pslo = ft.Dropdown(
            label = "数字伪本地化",           
            hint_text = "选择数字伪本地化方案，默认为“无”",
            options=[
                ft.dropdown.Option(key = 0, text = "无"),
                ft.dropdown.Option(key = 1, text = "使用①-⑨替代1-9"),
                ft.dropdown.Option(key = 2, text = "使用₀-₉或⁰-⁹交叉替换0-9")
            ]) 
    num_pslo.value = 0
    num_pslo = ft.Dropdown(
            label = "数字伪本地化",           
            hint_text = "选择数字伪本地化方案, 默认为“无”",
            value = 0, #默认为“无”
            options = [
                ft.dropdown.Option(key = 0, text = "无"),
                ft.dropdown.Option(key = 1, text = "使用①-⑨替代1-9"),
                ft.dropdown.Option(key = 2, text = "使用₀-₉或⁰-⁹交叉替换0-9")
            ]) 
    #----------#
    vowel_tx = ft.Text("重复元音次数(0代表不重复, 1代表双写, 以此类推): ",size=15)
    vowel_cs = ft.TextField(width = 150, label = "次数 (0-10)", value = 0, on_blur = vcs_check) 
    row_vow = ft.Row(spacing = 10, controls = [vowel_tx,vowel_cs])
    #----------#
    vis_con_cb = ft.Switch(label = r"翻译后隐藏%s, \n等控制字符", value = False)

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
            )
        )
    
    # 外观设置
    opt_look = ft.Row(
            [
                ft.Icon(name = ft.icons.PALETTE_OUTLINED),
                ft.Text("外观", size = 22)
            ]
        )
    #----------#
    theme = ft.Dropdown(
            label = "亮暗模式",
            hint_text = "亮暗模式",
            options=[
                ft.dropdown.Option(key = 0, text = "亮色"),
                ft.dropdown.Option(key = 1, text = "暗色"),
                ft.dropdown.Option(key = 2, text = "跟随系统")
            ],
            on_change = theme_changed) 
    theme.value = 2
    #----------#
    sch_text = ft.Text("配色", size = 20)
    scheme = ft.RadioGroup(value = 0, content = ft.Row([
            ft.Radio(
                value = 0,
                label = "蓝色",
                fill_color = ft.colors.BLUE_800,
            ),
            ft.Radio(
                value = 1,
                label = "粉色",
                fill_color = ft.colors.PINK_700,
            ),
            ft.Radio(
                value = 2,
                label = "绿色",
                fill_color = ft.colors.GREEN_700,
            ),
            ft.Radio(
                value = 3,
                label = "巧克力色",
                fill_color = ft.colors.BROWN,
            ),
            ft.Radio(
                value = 4,
                label = "紫色",
                fill_color = ft.colors.DEEP_PURPLE,
            )
        ]), on_change = sch_changed)
    #----------#
    opacity_text = ft.Text("窗口透明度", size = 20)
    page.opacity_slider = ft.Slider(min = 50, max = 100, width=400, divisions = 50, label = "{value}%", on_change = opacity_slider_changed, value = 100)
    opacity_bar = ft.Row(controls = [opacity_text, ft.Icon(ft.icons.OPACITY), page.opacity_slider, ft.Icon(ft.icons.WATER_DROP)])

    look_opt_card = ft.Card(
            content = ft.Container(
                content = ft.Column(
                    [
                        theme,
                        sch_text,
                        scheme,
                        opacity_bar
                    ]
                ),
                padding = 15
            )
        )
    
    # 关于内容
    abt = ft.Row(
            [
                ft.Icon(name = ft.icons.INFO_OUTLINE),
                ft.Text("关于", size = 22)
            ]
        )    
    about = ft.Text(basic_info.about_text, size = 15, selectable = True)
    upd_bar = ft.Row(
        controls = [
            ft.TextButton("更新日志", icon = ft.icons.UPDATE, on_click = open_upd),
            ft.TextButton("检查更新", icon = ft.icons.UPLOAD_OUTLINED, on_click = check_for_update),
            ft.TextButton("网页版",icon=ft.icons.OPEN_IN_BROWSER_ROUNDED,on_click = open_with_browser),
            ft.TextButton("项目仓库",icon=ft.icons.COLLECTIONS_BOOKMARK_OUTLINED,on_click = open_project_repo),
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
            )
        )
    set_col = ft.Column(scroll=ft.ScrollMode.ALWAYS,controls=[
        opt_pslo,opt_pslo_detail,pslo_opt_card,
        opt_look,look_opt_card,
        abt,abt_card])
    set_page = ft.Container(
        height=page.window_height-90,
        content = set_col,
        visible=False)
    main_area = ft.Column(height= page.window_height-90,controls=[home_page,his_page,set_page])
    
    #导航栏
    rail = ft.NavigationRail(
        selected_index=0,
        height=page.window_height-90,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=50,
        min_extended_width=100,
        group_alignment = -1.0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_ROUNDED, label="主页"
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.HISTORY_OUTLINED),
                selected_icon_content=ft.Icon(ft.icons.HISTORY_ROUNDED),
                label="历史记录",
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("设置"),
            ),
        ],
        on_change = rail_ctrl,
    )
    main_row = ft.Row(height=page.window_height-90, width=page.window_width,controls=[rail,main_area])
    page.add(titlebar, main_row)
    print("\033[0;34m[INFO] Window initialization completed\033[0m")

ft.app(target = main)
