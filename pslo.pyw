import flet as ft
import random
import pyperclip
import webbrowser

# 基本信息
ver = "v2.3p_experiment"
author = "Suntrise (STR)"
title = "伪本地化演示程序 " + ver + " by " + author

# 数据集
arra = ["ä", "ā", "á", "ǎ", "à", "ă", "å", "ǻ", "ã", "ǟ", "ǡ", "ǻ", "ȁ", "ȃ", "ȧ", "ᶏ", "ḁ", "ẚ", "ạ", "ả", "ấ", "ầ", "ẩ", "ẫ", "ậ", "ắ", "ằ", "ẳ", "ẵ", "ặ", "ɑ", "α", "ά", "ὰ", "ἀ", "ἁ", "ἂ", "ἃ", "ἆ", "ἇ", "ᾂ", "ᾃ", "ᾰ", "ᾱ", "ᾲ", "ᾳ", "ᾴ", "ᾶ", "ᾷ", "ⱥ", "𐓘", "𐓙", "𐓚"]
arraa = ["Ā", "Á", "Ǎ", "À", "Â", "Ã", "Ä", "Å", "Ǻ", "Ά", "Ă", "Δ", "Λ", "Д", "Ą"]
arrb = ["b", "ь", "в", "Ъ", "Б", "б", "β", "ƀ", "ƃ", "ɓ", "ᵬ", "ᶀ", "ḃ", "ḅ", "ḇ", "ꞗ", "ḃ"]
arrbb = ["ß", "฿", "Ḃ"]
arrc = ["c", "ç", "ς", "ĉ", "č", "ċ", "ć", "ĉ", "ċ", "ƈ", "ȼ", "¢", "ɕ", "ḉ", "ꞓ", "ꞔ"]
arrcc = ["Č", "Ç", "Ĉ", "Ć", "€", "Ċ", "Č", "¢"]
arrd = ["d", "ď", "đ", "₫", "ð", "δ", "ď"]
arrdd = ["Ď", "Ð", "Ḋ"]
arre = ["e", "ē", "é", "ě", "è", "ê", "ĕ", "ė", "ë", "ę", "з", "ε", "έ", "э", "℮"]
arree = ["E", "Ē", "É", "Ě", "È", "Ę", "Ё", "Σ", "Έ", "Є", "Э", "З", "Ė"]
arrf = ["f", "ƒ", "ḟ"]
arrff = ["F", "₣", "Ƒ", "Ḟ"]
arrg = ["ḡ", "ģ", "ǧ", "ĝ", "ğ", "ġ", "ǥ", "ǵ", "ɠ", "ᶃ", "ꞡ"]
arrgg = ["Ḡ", "Ǵ", "Ǧ", "Ĝ", "Ğ", "Ģ", "Ġ", "Ɠ", "Ǥ", "Ꞡ"]
arrh = ["ĥ", "ħ", "ђ", "н", "ḣ"]
arrhh = ["H", "Ĥ", "Ħ", "Ḣ"]
arri = ["ı", "ī", "í", "ǐ", "ì", "ĭ", "î", "ï", "ί", "į", "ΐ", "ι"]
arrii = ["Ī", "Í", "Ǐ", "Ì", "Î", "Ï", "Ĭ", "Ί", "ı", "İ"]
arrj = ["j"]
arrjj = ["J", "Ĵ"]
arrk = ["ƙ", "κ", "ķ", "ǩ"]
arrkk = ["К", "Ǩ", "Ķ"]
arrl = ["ŀ", "ļ", "ℓ", "ĺ", "ļ", "ľ", "ł", "₺"]
arrll = ["Ŀ", "£", "Ļ", "Ł", "Ĺ", "Ľ"]
arrm = ["m", "₥", "м", "ṁ"]
arrmm = ["M", "Ṁ"]
arrn = ["ń", "ň", "ŉ", "η", "ή", "и", "й", "ñ", "л", "п", "π", "ŋ", "ņ", "ṅ"]
arrnn = ["Ń", "Ň", "И", "Й", "Π", "Л", "Ñ", "Ŋ", "Ņ", "Ṅ"]
arro = ["ō", "ó", "ŏ", "ò", "ô", "õ", "ö", "ő", "σ", "ø", "ǿ", "ȯ"]
arroo = ["Ō", "Ó", "Ǒ", "Ò", "Ô", "Õ", "Ö", "Ό", "Θ", "Ǿ", "Ő", "Ȯ", "Ø", "Ω"]
arrp = ["p", "ρ", "ƥ", "φ", "ṗ"]
arrpp = ["P", "Þ", "₽", "Ṗ"]
arrq = ["q", "ʠ", "ɋ", "q"]
arrqq = ["Q", "Ɋ"]
arrr = ["ř", "ŗ", "г", "ѓ", "ґ", "я", "ṙ"]
arrrr = ["Ř", "Я", "Г", "Ґ", "Ŕ", "Ṙ", "₹"]
arrs = ["ś", "š", "ŝ", "ș", "ş", "ƨ", "ṡ"]
arrss = ["Š", "Ş", "Ș", "§", "$", "Ś", "Ṡ", "Ŝ"]
arrt = ["ț", "ţ", "ť", "ŧ", "т", "τ", "ṫ"]
arrtt = ["Ť", "Ţ", "Ț", "Ŧ", "Ţ", "Ṫ"]
arru = ["ū", "ú", "ǔ", "ù", "û", "ũ", "ů", "ų", "ü", "ǖ", "ǘ", "ǚ", "ǜ", "ύ", "ϋ", "ΰ", "µ", "ц", "џ"]
arruu = ["Ū", "Ǔ", "Ǖ", "Ǘ", "Ǚ", "Ǜ", "Ц", "Û", "Ú", "Ŭ," ,"Ű" ,"Ù" ,"Ů" ,"Ų"]
arrv = ["ν"]
arrvv = ["V", "V", "Ṽ", "Ṿ", "Ꝟ"]
arrw = ["ẃ", "ẁ", "ẅ", "ŵ", "ш", "щ", "ω", "ώ", "ẇ"]
arrww = ["Ẁ", "Ẃ", "Ẅ", "Ŵ", "Ш", "Щ", "₩", "Ẇ"]
arrx = ["x", "ж", "ẋ"]
arrxx = ["X", "Ж", "Ẋ"]
arry = ["y", "ỳ", "ŷ", "ч", "γ", "ẏ", "ÿ", "ý", "У", "Ў"]
arryy = ["Ϋ", "Ẏ", "Ŷ", "Ỳ", "Ύ", "Ψ", "￥", "Ч", "Ý"]
arrz = ["z", "ź", "ż", "ž", "ƶ", "ȥ", "ʐ", "ᵶ", "ᶎ", "ẑ", "ẓ", "ẕ", "ⱬ", "ż", "ζ"]
arrzz = ["Z", "Ź", "Ż", "Ž", "Ƶ", "Ȥ", "Ẓ", "Ẕ", "Ẑ", "Ⱬ", "Ż", "Ʒ", "Ǯ"]
arr1 = ["1", "₁", "¹"]
arr2 = ["2", "₂", "²"]
arr3 = ["3", "₃", "³"]
arr4 = ["4", "₄", "⁴"]
arr5 = ["5", "₅", "⁵"]
arr6 = ["6", "₆", "⁶"]
arr7 = ["7", "₇", "⁷"]
arr8 = ["8", "₈", "⁸"]
arr9 = ["9", "₉", "⁹"]
arr0 = ["0", "₀", "⁰"]
arral = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# 定义内容
what_text = "伪本地化(pseudo-localization, 语言环境名称为 qps-ploc, qps-plocm, qps-ploca, en-XA, en-XB), \n是通过模拟本地化过程, 以有效地调查在本地化中出现的问题\n(如字符无法正常显示, 或因字符串过长而导致语段显示不完整等）。\n在伪本地化过程中, 英文字母会被替换为来自其他语言的重音符号和字符。\n(例如, 字母 a 可以被 αäáàāāǎǎăăåå 中的任何一个替换), 还会添加分隔符等以增加字符串长度。\n例: “Windows Photo Gallery (Windows 照片库)”→“ [1iaT9][ Ẅĭпðøωś Þнôтŏ Ģάŀļєяÿ !!! !] ”\n更多信息: \nhttps://docs.microsoft.com/zh-cn/globalization/methodology/pseudolocalization, \nhttps://zhuanlan.zhihu.com/p/613293858"
about_text = "伪本地化演示程序 " + ver + "\n作者：" + author + "\n使用到的第三方库：\n   flet - UI库\n   django papercilp - 复制功能库"

# 主程序
def main(page: ft.Page):
    # 伪本地化
    def pslo(e):
        i = 0
        m = 0
        n = 0
        pstr = page.pstype.value
        res = ''
        if str != "":
            for l in pstr:
                i += 1
                if num_pslo.value == "2":
                    al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz)).replace('1',random.choice(arr1)).replace('2',random.choice(arr2)).replace('3',random.choice(arr3)).replace('4',random.choice(arr4)).replace('5',random.choice(arr5)).replace('6',random.choice(arr6)).replace('7',random.choice(arr7)).replace('8',random.choice(arr8)).replace('9',random.choice(arr9)).replace('0',random.choice(arr0))
                else:
                    if num_pslo.value == "1":
                        al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz)).replace('1','①').replace('2','②').replace('3','③').replace('4','④').replace('5','⑤').replace('6','⑥').replace('7','⑦').replace('8','⑧').replace('9','⑨')
                    else:
                        al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz))
                res += al
        
        if suf_way.value == "1":
            suf = ""
            while i > 2 and n < (i/7): 
                suf = suf+"!"  
                n += 1
                if n % 3 == 0 & n != int(i/7+1):
                   suf = suf+" "
           
            res = "["+ res +" " +suf +"]";  
            n = 0
            suf = ""

        if hash_cb.value == True:
            hash_id = ""
            while m<5:
                hash_id = hash_id + random.choice(arral)
                
                m += 1

            res = "[" + hash_id + "]" +res
            hash_id = ""
            m = 0
          
        page.result.value = res
        res = ''
        page.update()  
    
    # 打开“什么是伪本地化”窗口
    def open_what(e):
        page.dialog = what_dlg
        what_dlg.open = True
        page.update()  
    
    # 关闭“什么是伪本地化”窗口
    def close_what(e):
        what_dlg.open = False
        page.update()

    # 打开“关于”窗口
    def open_about(e):
        page.dialog = about_dlg
        about_dlg.open = True
        page.update()  
    
    # 关闭“关于”窗口
    def close_about(e):
        about_dlg.open = False
        page.update()

    # 复制文本
    def copy_text(e):
        pyperclip.copy(page.result.value)
        page.snack_bar = ft.SnackBar(ft.Text(f"已复制"))
        page.snack_bar.open = True
        page.update()

    # 打开网页版
    def open_with_browser(e):
        webbrowser.open_new("https://suntrise.github.io/pseudo/")

    # 打开项目仓库
    def open_project_repo(e):
        webbrowser.open_new("https://github.com/suntrise/Pseudo-localization-Demo")

    # “什么是伪本地化”窗口定义
    what_dlg = ft.AlertDialog(
        title = ft.Text("什么是伪本地化?"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content = ft.Text(what_text),
        actions=[
            ft.TextButton(icon=ft.icons.DONE_OUTLINED, text = "我知道啦",on_click = close_what)
        ],
        actions_alignment = ft.MainAxisAlignment.END,
    ) 
    
    # “关于”窗口定义
    about_dlg = ft.AlertDialog(
        title = ft.Text("关于"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content = ft.Text(about_text),
        actions = [
            ft.TextButton(icon=ft.icons.DONE_OUTLINED, text = "确定",on_click=close_about)
        ],
        actions_alignment = ft.MainAxisAlignment.END,
    ) 
         
    # 用户界面
    page.title = title
    page.window_left = 200
    page.window_top = 100
    page.window_width = 700
    page.window_height = 590
    page.theme = ft.Theme(
         font_family="Microsoft Yahei",
         color_scheme_seed=ft.colors.BLUE
         )
    page.scroll = ft.ScrollMode.ALWAYS
    page.appbar = ft.AppBar(
        leading_width = 40,
        title = ft.Text("伪本地化演示", size = 20),
        actions=[
            ft.PopupMenuButton(
                items=[
                ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.OPEN_IN_BROWSER_OUTLINED),
                            ft.Text("网页版")
                        ]),
                       on_click = open_with_browser
                ),
                ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.COLLECTIONS_BOOKMARK_OUTLINED),
                            ft.Text("项目仓库")
                        ]),
                       on_click = open_project_repo
                ),
                ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.QUESTION_MARK_OUTLINED),
                            ft.Text("什么是伪本地化")
                        ]),
                       on_click = open_what
                ),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(                
                        content = ft.Row(
                        [
                            ft.Icon(ft.icons.INFO_OUTLINE),
                            ft.Text("关于")
                        ]),
                       on_click = open_about
                ),
                ]
            ),
        ],
    ) 

    # 伪本地化区
    page.pstype = ft.TextField(hint_text = "在这里输入要翻译的内容~", text_size =15, multiline = True, max_lines = 5)
    page.result = ft.TextField(hint_text = "结果会显示在这里~", text_size = 15, multiline = True, max_lines = 5, read_only = True)
    pslo_btn = ft.FilledButton(
        "伪本地化!",
        icon = ft.icons.TRANSLATE_OUTLINED,
        tooltip = "将您所填写的内容伪本地化, 每次点击效果都不太一样哦",
        on_click = pslo     
        )
    copy_btn = ft.FilledTonalButton(
        "复制",
        icon = ft.icons.COPY,
        tooltip = "将生成内容添加到设备剪切板",
        on_click = copy_text     
        )
    
    rowPSLO = ft.Row(spacing = 10, controls = [pslo_btn, copy_btn])

    # 设置区
    option = ft.Row([
        ft.Icon(name = ft.icons.SETTINGS_OUTLINED, size = 20),
        ft.Text("设置", size = 20)
    ])
    suf_way = ft.Dropdown(
            label = "前后缀",
            hint_text = "选择前后缀方案，默认为“不添加前后缀”",
            options=[
                ft.dropdown.Option(key = 0, text = "不添加前后缀"),
                ft.dropdown.Option(key = 1, text = "[中括号+感叹号括起来 (微软式伪本地化)!!!]")
            ])
    hash_cb = ft.Switch(label = "[Abc12]添加伪 Hash ID (资源标识符) (由一定位数的字母 + 数字所构成的字符串)", tooltip = "启用后，将为伪本地化内容添加伪Hash ID", value = False)
    num_pslo = ft.Dropdown(
            label = "数字伪本地化",
            hint_text = "选择数字伪本地化方案，默认为“无”",
            options=[
                ft.dropdown.Option(key = 0, text = "无"),
                ft.dropdown.Option(key = 1, text = "使用①-⑨替代1-9"),
                ft.dropdown.Option(key = 2, text = "使用₀-₉或⁰-⁹交叉替换0-9 (更强的随机性)")
            ]) 
    page.add(page.pstype, page.result, rowPSLO, option, suf_way, hash_cb, num_pslo)

ft.app(target=main)
