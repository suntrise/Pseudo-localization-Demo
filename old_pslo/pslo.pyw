import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import webbrowser

ver="v1.1p"
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

class win(QMainWindow):
    def __init__(self):
        super(win, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        fonte = QFont()
        fonte.setFamily("微软雅黑")
        fonte.setPointSize(11)
        fontres = QFont()
        fontres.setFamily("微软雅黑")
        fontres.setPointSize(11)
        fontbtn = QFont()
        fontbtn.setFamily("微软雅黑")
        fontbtn.setPointSize(12)

        self.setGeometry(400, 200, 700, 500)
        self.setWindowTitle('伪本地化演示程序')
        menubar = self.menuBar()
        whatAct = QAction('&什么是伪本地化？', self)
        aboutAct = QAction('&关于', self)        
        helpMenu = menubar.addMenu('帮助')
        webAct = menubar.addAction('网页版')
        githubAct = menubar.addAction('Github')
        helpMenu.addAction(whatAct)
        helpMenu.addAction(aboutAct)
        aboutAct.triggered.connect(self.about)
        whatAct.triggered.connect(self.what)
        webAct.triggered.connect(self.web)
        githubAct.triggered.connect(self.github)
        title = QtWidgets.QLabel(self)
        title.setText("伪本地化演示程序 "+ver)
        title.setFont(font)
        title.adjustSize()
        title.move(20, 50)
        self.pstype = QtWidgets.QTextEdit(self)
        self.pstype.setFont(fonte)
        self.pstype.setFixedWidth(300)
        self.pstype.setFixedHeight(200)
        self.pstype.setPlaceholderText("在这里输入要翻译的内容~")
        self.pstype.move(20, 120)
        self.result = QtWidgets.QTextEdit(self)
        self.result.setFont(fontres)
        self.result.setFixedWidth(300)
        self.result.setFixedHeight(200)
        self.result.setReadOnly(True)
        self.result.setPlaceholderText("结果会显示在这里~")
        self.result.move(350, 120)
        self.btn = QtWidgets.QPushButton('翻译成伪语言',self)
        self.btn.setFont(fontbtn)
        self.btn.setFixedWidth(180)
        self.btn.setFixedHeight(50)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.pslo)
        self.btn.move(20, 340)
        self.show()

    def pslo(self):
          self.str = self.pstype.toPlainText()
          res = ''
          for i in self.str:
              al = i.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz))

              res += al
          self.result.setPlainText(res)
          res = ''
          '''self.result.setPlainText(res)'''
                                             
    def about(self):
        QtWidgets.QMessageBox.about(self, "关于","伪本地化演示程序 "+ver+"<br> 作者：STR")

    def what(self):
        QtWidgets.QMessageBox.about(self, "什么是伪本地化？","伪本地化（pseudo-localization，语言环境名称为 qps-ploc, qps-plocm, qps-ploca, en-XA, en-XB），是通过模拟本地化过程，以有效地调查在本地化中出现的问题（如字符无法正常显示，或因字符串过长而导致语段显示不完整等）。<br>在伪本地化过程中，英文字母会被替换为来自其他语言的重音符号和字符。（例如，字母 a 可以被 αäáàāāǎǎăăåå 中的任何一个替换。），还会添加分隔符等以增加字符串长度。<br>举例：“Windows Photo Gallery（Windows 照片库）”→“ [1iaT9][ Ẅĭпðøωś Þнôтŏ Ģάŀļєяÿ !!! !] ”")
    
    def web(self):
        webbrowser.open_new('https://suntrise.github.io/pseudo/')

    def github(self):
        webbrowser.open_new('https://github.com/suntrise/Pseudo-localization-Demo')
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    pseudo = win()
    sys.exit(app.exec_())
