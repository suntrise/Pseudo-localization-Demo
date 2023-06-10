import flet as ft
import random

ver="v2.1p"
author="Suntrise (STR)"
arra=["ä","ā","á","ǎ","à","ă","å","ǻ","ã","ǟ","ǡ","ǻ","ȁ","ȃ","ȧ","ᶏ","ḁ","ẚ","ạ","ả","ấ","ầ","ẩ","ẫ","ậ","ắ","ằ","ẳ","ẵ","ặ","ɑ","α","ά","ὰ","ἀ","ἁ","ἂ","ἃ","ἆ","ἇ","ᾂ","ᾃ","ᾰ","ᾱ","ᾲ","ᾳ","ᾴ","ᾶ","ᾷ","ⱥ","𐓘","𐓙","𐓚"]
arraa=["Ā","Á","Ǎ","À","Â","Ã","Ä","Å","Ǻ","Ά","Ă","Δ","Λ","Д","Ą"]
arrb=["b","ь","в","Ъ","Б","б","β","ƀ","ƃ","ɓ","ᵬ","ᶀ","ḃ","ḅ","ḇ","ꞗ"]
arrbb=["ß","฿"]
arrc=["c","ç","ς","ĉ","č","ċ","ć","ĉ","ċ","ƈ","ȼ","¢","ɕ","ḉ","ꞓ","ꞔ"]
arrcc=["Č","Ç","Ĉ","Ć","€"]
arrd=["d","ď","đ","₫","ð","δ"]
arrdd=["Ď","Ð"]
arre=["e","ē","é","ě","è","ê","ĕ","ė","ë","ę","з","ε","έ","э","℮"]
arree=["E","Ē","É","Ě","È","Ĕ","Ё","Σ","Έ","Є","Э","З"]
arrf=["f","ƒ"]
arrff=["F","₣"]
arrg=["ḡ","ģ","ǧ","ĝ","ğ","ġ","ǥ","ǵ","ɠ","ᶃ","ꞡ"]
arrgg=["Ḡ","Ǵ","Ǧ","Ĝ","Ğ","Ģ","Ġ","Ɠ","Ǥ","Ꞡ"]
arrh=["ĥ","ħ","ђ","н"]
arrhh=["H","Ĥ","Ħ"]
arri=["ı","ī","í","ǐ","ì","ĭ","î","ï","ί","į","ΐ","ι"]
arrii=["Ī","Í","Ǐ","Ì","Î","Ï","Ĭ","Ί"]
arrj=["j"]
arrjj=["J","Ĵ"]
arrk=["ƙ","κ"]
arrkk=["К"]
arrl=["ŀ","ļ","ℓ","ĺ","ļ","ľ","ł"]
arrll=["Ŀ","£","Ļ","Ł","Ĺ"]
arrm=["m","₥","м"]
arrmm=["M"]
arrn=["ń","ň","ŉ","η","ή","и","й","ñ","л","п","π"]
arrnn=["Ń","Ň","И","Й","Π","Л"]
arro=["ō","ó","ŏ","ò","ô","õ","ö","ő","σ","ø","ǿ"]
arroo=["Ō","Ó","Ǒ","Ò","Ô","Õ","Ö","Ό","Θ","Ǿ"]
arrp=["p","ρ","ƥ","φ"]
arrpp=["P","Þ","₽"]
arrq=["q","ʠ", "ɋ"]
arrqq=["Q","Ɋ"]
arrr=["ř","ŗ","г","ѓ","ґ","я"]
arrrr=["Ř","Я","Г","Ґ"]
arrs=["ś","š","ŝ","ș","ş","ƨ"]
arrss=["Š","Ş","Ș","§"]
arrt=["ț","ţ","ť","ŧ","т","τ"]
arrtt=["Ť","Ţ","Ț","Ŧ"]
arru=["ū","ú","ǔ","ù","û","ũ","ů","ų","ü","ǖ","ǘ","ǚ","ǜ","ύ","ϋ","ΰ","µ","ц","џ"]
arruu=["Ū","Ǔ","Ǖ","Ǘ","Ǚ","Ǜ","Ц"]
arrv=["ν"]
arrvv=["V","V","Ṽ","Ṿ","Ꝟ"]
arrw=["ẃ","ẁ","ẅ","ŵ","ш","щ","ω","ώ"]
arrww=["Ẁ","Ẃ","Ẅ","Ŵ","Ш","Щ"]
arrx=["x","ж"]
arrxx=["X","Ж"]
arry=["y","ỳ","ŷ","ч","γ"]
arryy=["Ϋ","Ÿ","Ŷ","Ỳ","Ύ","Ψ","￥","У","Ў","Ч"]
arrz=["z","ź","ż","ž","ƶ","ȥ","ʐ","ᵶ","ᶎ","ẑ","ẓ","ẕ","ⱬ"]
arrzz=["Z","Ź","Ż","Ž","Ƶ","Ȥ","Ẓ","Ẕ","Ẑ","Ⱬ"]
arral=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0"]
what_text = "伪本地化（pseudo-localization，语言环境名称为 qps-ploc, qps-plocm, qps-ploca, en-XA, en-XB），是通过模拟本地化过程，以有效地调查在本地化中出现的问题（如字符无法正常显示，或因字符串过长而导致语段显示不完整等）。\n在伪本地化过程中，英文字母会被替换为来自其他语言的重音符号和字符。（例如，字母 a 可以被 αäáàāāǎǎăăåå 中的任何一个替换。），还会添加分隔符等以增加字符串长度。\n举例：“Windows Photo Gallery（Windows 照片库）”→“ [1iaT9][ Ẅĭпðøωś Þнôтŏ Ģάŀļєяÿ !!! !] ”\n更多信息：https://docs.microsoft.com/zh-cn/globalization/methodology/pseudolocalization, https://zhuanlan.zhihu.com/p/613293858\n该网页演示了伪本地化的一部分，即用不同的字符替换英文字母和添加分隔符。\n更多功能将在之后更新，感谢大家的支持！"
about_text = "伪本地化演示程序 v2.1p \n作者：Suntrise（STR）"
def main(page: ft.Page):
    def pslo(e):
        i = 0
        m = 0
        n = 0
        pstr = page.pstype.value
        res = ''
        if str != "":
            for l in pstr:
                i += 1
                al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz))
                res += al
        
        if suf_way.value == "1":
            suf = ""
            while i>2 and n < (i/7): 
                suf = suf+"!"  
                n += 1
                if n % 3==0 & n != int(i/7+1):
                   suf =suf+" "
           
            res = "["+ res +" " +suf +"]";  
            n=0;
            suf=""

        if hash_cb.value == True:
            hash_id = ""
            while m<5:
                hash_id = hash_id + random.choice(arral)
                
                m += 1

            res = "[" + hash_id + "]" +res
            hash_id = ""
            m=0
          
        page.result.value = res
        res = ''
        page.update()  
    
    def open_what(e):
        page.dialog = what_dlg
        what_dlg.open = True
        page.update()  
    
    def close_what(e):
        what_dlg.open = False
        page.update()

    def open_about(e):
        page.dialog = about_dlg
        about_dlg.open = True
        page.update()  
    
    def close_about(e):
        about_dlg.open = False
        page.update()

    what_dlg = ft.AlertDialog(
        title = ft.Text("什么是伪本地化？"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content = ft.Text(what_text),
        actions=[
            ft.TextButton("我知道啦",on_click=close_what)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape = ft.RoundedRectangleBorder(radius=5)
    )  
    about_dlg = ft.AlertDialog(
        title = ft.Text("关于"), on_dismiss=lambda e: print("Dialog dismissed!"),
        content = ft.Text(about_text),
        actions=[
            ft.TextButton("确定",on_click=close_about)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        shape = ft.RoundedRectangleBorder(radius=5)
    ) 
         
    page.title = "伪本地化演示程序 v2.1p"
    page.window_left = 200
    page.window_top = 100
    page.window_width = 800
    page.window_height = 550
    page.theme = ft.Theme(
         font_family="Microsoft Yahei",
         color_scheme_seed=ft.colors.BLUE
         )
    page.scroll = ft.ScrollMode.ALWAYS
    page.appbar = ft.AppBar(
        leading_width=30,
        title=ft.Text("伪本地化演示程序 v2.1p By STR"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(                
                        content=ft.Row(
                        [
                            ft.Icon(ft.icons.QUESTION_MARK),
                            ft.Text("什么是伪本地化？"),
                        ]),
                       on_click= open_what
                ),
                    ft.PopupMenuItem(                
                        content=ft.Row(
                        [
                            ft.Icon(ft.icons.INFO_OUTLINE_ROUNDED),
                            ft.Text("关于"),
                        ]),
                       on_click= open_about
                ),
                ]
            ),
        ],
    ) 
    web_btn = ft.TextButton(
        "网页版", 
        icon=ft.icons.OPEN_IN_BROWSER,
        url = "https://suntrise.github.io/pseudo/"    
        )
    git_btn = ft.TextButton(
        "项目主页", 
        icon=ft.icons.HOME,
        url = "https://github.com/suntrise/Pseudo-localization-Demo"    
        )
    what_btn = ft.TextButton(
        "什么是伪本地化", 
        icon=ft.icons.QUESTION_MARK,
        on_click = open_what  
        )
    row = ft.Row(spacing=5, controls=[web_btn,git_btn,what_btn])

    page.pstype = ft.TextField(hint_text="在这里输入要翻译的内容~",text_size=15,multiline=True,max_lines=5)
    page.result = ft.TextField(hint_text="结果会显示在这里~",text_size=15,multiline=True,max_lines=5,read_only=True)
    pslo_btn = ft.ElevatedButton(
        content = ft.Text(value = "进行伪本地化",size=18),
        style=ft.ButtonStyle(
        shape={
            ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=5),
            }            
        ),
        height=50,
        color="#ffffff",
        bgcolor="#0078DC",
        on_click = pslo     
        )
    option = ft.Text("设置：",size=25)
    suf_way = ft.Dropdown(
            label="前后缀",
            hint_text="前后缀",
            options=[
                ft.dropdown.Option(key=0,text="不添加前后缀"),
                ft.dropdown.Option(key=1,text="[中括号+感叹号括起来（微软式伪本地化）!!!]")
            ])
    hash_cb = ft.Checkbox(label="[Abc12]添加伪 Hash ID (资源标识符)(由一定位数的字母+数字所构成的字符串)", value=False)
       
    page.add(row,page.pstype,page.result,pslo_btn,option,suf_way,hash_cb)

ft.app(target=main)
