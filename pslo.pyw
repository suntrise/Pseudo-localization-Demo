import flet as ft # 界面库
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

# 细节定义
edge = ft.Divider(height = 1, thickness = 1.5)
divider = ft.Divider(height = 9, thickness = 1)

print('\033[0;34m[INFO] Python version: {}\033[0m'.format(sys.version))
print("\033[0;34m[INFO] PSLO version: " + basic_info.ver + "\033[0m")
print("\033[0;32m[DONE] Basic initialization completed\033[0m")

# 主程序
def main(page: ft.Page):

    # 原pslo函数已迁移至lib/pslo_work.py
    def ccs_check(e):
        if cus_cs.value.isdigit() == False:
           cus_cs.value = 7; 
        page.update()
        
    def psf_check(e):
        if suf_way.value == "3":
            cus_ps.visible = True
        else:
            cus_ps.visible = False
        page.update()
    
    # 伪本地化
    def pslo(e):
        global pshis
        page.result.value = pslo_work.pslo(page.pstype.value, xab.value, num_pslo.value, vowel_cs.value, suf_way.value,cus_pre.value,cus_suf.value,cus_re.value,cus_cs.value, hash_cb.value, hash_ws.value)
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
    
    # 导入文件
    def ps_files(e: ft.FilePickerResultEvent):
        psfile = ", ".join(map(lambda f: f.path, e.files)) if e.files else "ERR"
        if psfile != "ERR":
            page.snack_bar = ft.SnackBar(ft.Text("检测到文件: " + psfile)) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(UL)\033[0m")
            with open(psfile) as psf:
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
        if svfile != "ERR":
            page.snack_bar = ft.SnackBar(ft.Text("已保存至: " + svfile)) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(SV)\033[0m")
            with open(svfile, "a", encoding = 'utf-8') as svf:
                svf.write(page.result.value)
                print("\033[0;32m[DONE] File saved:" + str(svfile) + "\033[0m")
        page.update()

    # 清除历史记录
    def clear_his(e):
        pshis = ""
        history.value = "无记录"
        print("\033[0;32m[DONE] History is cleared\033[0m")
        page.snack_bar = ft.SnackBar(ft.Text(f"已清空")) # 提示栏
        page.snack_bar.open = True
        page.update()
        print("\033[0;34m[INFO] Snack bar pop-up(CH)\033[0m")
    
    # 导出历史记录
    def sv_his(e: ft.FilePickerResultEvent):
        svhis = e.path if e.path else "ERR"
        if svhis != "ERR":
            page.snack_bar = ft.SnackBar(ft.Text("已保存至: " + svhis)) # 提示栏
            page.snack_bar.open = True
            page.update()
            print("\033[0;34m[INFO] Snack bar pop-up(SV)\033[0m")
            with open(svhis, "a", encoding = 'utf-8') as svh:
                svh.write(history.value)
                print("\033[0;32m[DONE] File saved:" + str(svhis) + "\033[0m")
        page.update()    
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
        vcs=vowel_cs.value
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

    # “什么是伪本地化”窗口定义
    what_dlg = ft.AlertDialog(
        title = ft.Text("什么是伪本地化?"), on_dismiss = lambda e: print("\033[0;34m[INFO] Dialog dismissed(WHT)\033[0m"),
        content = ft.Markdown(basic_info.what_text, selectable = True),
        actions = [
            ft.TextButton("我知道啦", icon = ft.icons.DONE, on_click = close_what)      
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
    page.title = basic_info.title
    page.window_left = 200
    page.window_top = 100
    page.window_height = 600
    page.window_width = 800 
    page.window_min_height = 400
    page.window_min_width = 760
    #page.window_title_bar_hidden = True
    #page.window_title_bar_buttons_hidden = True
    page.theme = ft.Theme(
         font_family = "Microsoft Yahei",
         color_scheme_seed = ft.colors.BLUE
         )
    page.scroll = ft.ScrollMode.ALWAYS
    # 应用栏定义
    page.appbar = ft.AppBar(
        leading_width = 30,
        title = ft.Text(basic_info.title),
        center_title = False,
        actions = [
            ft.PopupMenuButton(
                items = [
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.OPEN_IN_BROWSER),
                            ft.Text("网页版"),
                        ]),
                       on_click = open_with_browser
                    ),
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.COLLECTIONS_BOOKMARK_OUTLINED),
                            ft.Text("项目仓库"),
                        ]),
                       on_click = open_project_repo     
                    ),
                    ft.PopupMenuItem(), # 分隔
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.QUESTION_MARK_OUTLINED),
                            ft.Text("什么是伪本地化?"),
                        ]),
                       on_click = open_what
                    ),
                ]
            ),
        ],
    ) 

    # 主页区
    xab_text = ft.Text("伪本地化方式:",size=20)
    xab = ft.RadioGroup(value = "enxa",content=ft.Row([
    ft.Radio(value = "enxa", label = "en-XA (abc → ǻƀĉ)"),
    ft.Radio(value = "enxb", label = "en-XB (abc → cba)")]))
    what_btn = ft.TextButton(
        "什么是伪本地化", 
        icon = ft.icons.QUESTION_MARK_OUTLINED,
        on_click = open_what
        )
    XABrow = ft.Row(spacing = 10, controls = [xab_text,xab,what_btn])
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size =15, multiline = True, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = True, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
        "进行伪本地化!",
        icon = ft.icons.TRANSLATE_OUTLINED,
        tooltip = "将您所填写的内容伪本地化, 每次生成结果都会不一样哦",
        on_click = pslo     
        )
    
    copy_btn = ft.FilledTonalButton(
        "复制",
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
    row_pslo = ft.Row(spacing = 10, controls = [pslo_btn, copy_btn, lsfile])
    
    # 历史记录
    history = ft.Text("无记录", size = 18, selectable = True)
    save_his_dialog = ft.FilePicker(on_result = sv_his)
    his_opt = ft.Row(alignment = ft.MainAxisAlignment.END, controls = [
        save_his_dialog,
        ft.TextButton(
            "清空",
            icon = ft.icons.DELETE_FOREVER_OUTLINED,
            on_click = clear_his
        ),
        ft.TextButton(
            "导出记录",
            icon = ft.icons.FILE_DOWNLOAD,
            on_click = lambda _: save_his_dialog.save_file(allowed_extensions = ["txt"])
        ),
    ])
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
           ],on_change=psf_check) 
    cus_pre = ft.TextField(width=80,label="前缀",value="[")
    cus_suf = ft.TextField(width=80,label="后缀",value="]")
    cus_re = ft.TextField(label="在语段后重复添加……")
    cus_cs = ft.TextField(width=230,label="每隔多少个字符重复一次：",value=7,on_blur=ccs_check)
    cus_ps = ft.Row(spacing = 5, visible=False, controls = [cus_pre, cus_suf, cus_re, cus_cs])

    #----------#
    hash_cb = ft.Switch(label = "[Abc12]添加伪 Hash ID (资源标识符)(由一定位数的字母+数字所构成的字符串)", value = False, on_change = hash_check)
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
    dont_con_cb = ft.Switch(label = "[WIP]不翻译%s, \\n等控制字符", value = False, disabled = True)
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
    scheme = ft.RadioGroup(value = 0,content=ft.Row([
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
        ),])
        ,on_change = sch_changed)
    #----------#
    opacity_text = ft.Text("窗口透明度", size = 20)
    page.opacity_slider = ft.Slider(min = 50, max = 100, divisions = 50, label = "{value}%", on_change = opacity_slider_changed, value = 100)
    
    #关于内容
    abt = ft.Row(
            [
                ft.Icon(name = ft.icons.INFO_OUTLINE),
                ft.Text("关于", size = 22)
            ]
        )    
    about = ft.Text(basic_info.about_text, size = 15, selectable = True)
    upd_bar = ft.Row(
        controls=[
            ft.TextButton("更新日志", icon = ft.icons.UPDATE, on_click = open_upd),
            ft.TextButton("检查更新", icon = ft.icons.UPLOAD_OUTLINED, on_click = check_for_update)
        ]
    )

    # 标签
    tab = ft.Tabs(
        selected_index = 0,
        animation_duration = 200,
        tabs = [
            ft.Tab(
                text = "主界面",
                icon = ft.icons.HOME_OUTLINED,
                content = ft.Container(
                    ft.Column(spacing = 5, controls = [edge, XABrow, page.pstype, page.result, row_pslo])
                ),
            ),
            ft.Tab(
                text = "历史记录",
                icon = ft.icons.HISTORY_OUTLINED,
                content = ft.Column(spacing = 10, controls = [edge, his_opt, history]),
            ),
            ft.Tab(
                text = "设置",
                icon = ft.icons.SETTINGS_OUTLINED,
                content = ft.Column(spacing = 10, controls = [edge, opt_pslo, opt_pslo_detail, suf_way, cus_ps, row_hash, num_pslo, row_vow, dont_con_cb, divider, opt_look, theme, sch_text, scheme, opacity_text, page.opacity_slider, divider, abt, about, upd_bar]), 
            ),
        ]
    )
    page.add(tab)
    page.update()
    print("\033[0;32m[DONE] Window initialization completed\033[0m")

ft.app(target = main)
