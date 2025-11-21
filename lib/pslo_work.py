import random
from lib import log # 日志输出库

# 预备输出
log.out(0, "PSLO Translate Module ready...")

# 变量初始化
suf = ""

# 字符库
arra = ["ä", "ā", "á", "ǎ", "à", "ă", "å", "ǻ", "ã", "ǟ", "ǡ", "ǻ", "ȁ", "ȃ", "ȧ", "ᶏ", "ḁ", "ẚ", "ạ", "ả", "ấ", "ầ", "ẩ", "ẫ", "ậ", "ắ", "ằ", "ẳ", "ẵ", "ặ", "ɑ", "α", "ά", "ὰ", "ἀ", "ἁ", "ἂ", "ἃ", "ἆ", "ἇ", "ᾂ", "ᾃ", "ᾰ", "ᾱ", "ᾲ", "ᾳ", "ᾴ", "ᾶ", "ᾷ", "ⱥ", "𐓘", "𐓙", "𐓚"]
arraa = ["Ā", "Á", "Ǎ", "À", "Â", "Ã", "Ä", "Å", "Ǻ", "Ά", "Ă", "Δ", "Λ", "Д", "Ą", "Ắ", "Ặ", "Ằ", "Ẳ", "Ẵ", "Ấ", "Ậ", "Ầ", "Ẩ", "Ẫ", "Ã"]
arrb = ["b", "ь", "в", "Ъ", "Б", "б", "β", "ƀ", "ƃ", "ɓ", "ᵬ", "ᶀ", "ḃ", "ḅ", "ḇ", "ꞗ", "ḃ", "ъ"]
arrbb = ["ß", "฿", "Ḃ", "₿"]
arrc = ["c", "ç", "ς", "ĉ", "č", "ċ", "ć", "ĉ", "ċ", "ƈ", "ȼ", "¢", "ɕ", "ḉ", "ꞓ", "ꞔ"]
arrcc = ["Č", "Ç", "Ĉ", "Ć", "€", "Ċ", "Č", "¢", "∁"]
arrd = ["d", "ď", "đ", "₫", "ð", "δ", "ď", "ð"]
arrdd = ["Ď", "Ð", "Ḋ"]
arre = ["e", "ē", "é", "ě", "è", "ê", "ĕ", "ė", "ë", "ę", "з", "ε", "έ", "э", "℮", "ẹ", "ẻ", "ẽ", "ế", "ề", "ể", "ễ", "ệ", "ә", "ӟ"]
arree = ["E", "Ē", "É", "Ě", "È", "Ę", "Ё", "Σ", "Έ", "Є", "Э", "З", "Ė", "Ξ", "ξ", "Ê", "Ế", "Ệ", "Ề", "Ể", "Ễ", "Ẹ", "Ẻ", "Ę", "Ә"]
arrf = ["f", "ƒ", "ḟ"]
arrff = ["F", "₣", "Ƒ", "Ḟ", "Ғ"]
arrg = ["ḡ", "ģ", "ǧ", "ĝ", "ğ", "ġ", "ǥ", "ǵ", "ɠ", "ᶃ", "ꞡ"]
arrgg = ["Ḡ", "Ǵ", "Ǧ", "Ĝ", "Ğ", "Ģ", "Ġ", "Ɠ", "Ǥ", "Ꞡ"]
arrh = ["ĥ", "ħ", "ђ", "н", "ḣ", "ң", "һ"]
arrhh = ["H", "Ĥ", "Ħ", "Ḣ", "Ћ", "Ђ", "Ң"]
arri = ["ı", "ī", "í", "ǐ", "ì", "ĭ", "î", "ï", "ί", "į", "ΐ", "ι", "ỉ", "ị"]
arrii = ["Ī", "Í", "Ǐ", "Ì", "Î", "Ï", "Ĭ", "Ί", "ı", "İ", "Ị", "Ỉ"]
arrj = ["j"]
arrjj = ["J", "Ĵ"]
arrk = ["ƙ", "κ", "ķ", "ǩ", "қ"]
arrkk = ["К", "Ǩ", "Ķ", "Қ"]
arrl = ["ŀ", "ļ", "ℓ", "ĺ", "ļ", "ľ", "ł", "₺"]
arrll = ["Ŀ", "£", "Ļ", "Ł", "Ĺ", "Ľ"]
arrm = ["m", "₥", "м", "ṁ"]
arrmm = ["M", "Ṁ"]
arrn = ["ń", "ň", "ŉ", "η", "ή", "и", "й", "ñ", "л", "п", "π", "ŋ", "ņ", "ṅ", "ӥ"]
arrnn = ["Ń", "Ň", "И", "Й", "Π", "Л", "Ñ", "Ŋ", "Ņ", "Ṅ"]
arro = ["ō", "ó", "ŏ", "ò", "ô", "õ", "ö", "ő", "σ", "ø", "ǿ", "ȯ", "ơ", "ọ", "ỏ", "ố", "ồ", "ổ", "ỗ", "ộ", "ớ", "ờ", "ở", "ỡ", "ợ", "ө", "ӧ"]
arroo = ["Ō", "Ó", "Ǒ", "Ò", "Ô", "Õ", "Ö", "Ό", "Θ", "Ǿ", "Ő", "Ȯ", "Ø", "Ω", "θ", "Ф", "Ố", "Ộ", "Ồ", "Ổ", "Ỗ", "Ọ", "Ỏ", "Ơ", "Ớ", "Ợ", "Ờ", "Ở", "Ỡ", "Ő", "Ǫ", "Ǿ", "Ө"]
arrp = ["p", "ρ", "ƥ", "φ", "ṗ"]
arrpp = ["P", "Þ", "₽", "Ṗ"]
arrq = ["q", "ʠ", "ɋ", "q", "ς"]
arrqq = ["Q", "Ɋ"]
arrr = ["ř", "ŗ", "г", "ѓ", "ґ", "я", "ṙ", "ŕ"]
arrrr = ["Ř", "Я", "Г", "Ґ", "Ŕ", "Ṙ", "₹"]
arrs = ["ś", "š", "ŝ", "ș", "ş", "ƨ", "ṡ"]
arrss = ["Š", "Ş", "Ș", "§", "$", "Ś", "Ṡ", "Ŝ", "₴"]
arrt = ["ț", "ţ", "ť", "ŧ", "т", "τ", "ṫ", "т"]
arrtt = ["Ť", "Ţ", "Ț", "Ŧ", "Ţ", "Ṫ", "Ŧ"]
arru = ["ū", "ú", "ǔ", "ù", "û", "ũ", "ů", "ų", "ü", "ǖ", "ǘ", "ǚ", "ǜ", "ύ", "ϋ", "ΰ", "µ", "ц", "џ", "ŭ", "ư", "ű", "ụ", "ủ", "ứ", "ừ", "ử", "ữ", "ự"]
arruu = ["Ū", "Ǔ", "Ǖ", "Ǘ", "Ǚ", "Ǜ", "Ц", "Û", "Ú", "Ŭ" ,"Ű" ,"Ù" ,"Ů" ,"Ų", "∪", "Ụ", "Ủ", "Ư", "Ứ", "Ự", "Ừ", "Ử", "Ữ", "Ũ"]
arrv = ["ν"]
arrvv = ["V", "V", "Ṽ", "Ṿ", "Ꝟ"]
arrw = ["ẃ", "ẁ", "ẅ", "ŵ", "ш", "щ", "ω", "ώ", "ẇ"]
arrww = ["Ẁ", "Ẃ", "Ẅ", "Ŵ", "Ш", "Щ", "₩", "Ẇ"]
arrx = ["x", "ж", "ẋ", "ӝ"]
arrxx = ["X", "Ж", "Ẋ", "Ӝ"]
arry = ["y", "ỳ", "ŷ", "ч", "γ", "ẏ", "ÿ", "ý", "У", "Ў", "ỵ", "ỷ", "ỹ", "ұ", "ҷ", "ӵ"]
arryy = ["Ϋ", "Ẏ", "Ŷ", "Ỳ", "Ύ", "Ψ", "￥", "Ч", "Ý", "Ỵ", "Ỷ", "Ȳ", "Ỹ"]
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
arrba = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
arrnum = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# 伪本地化
def pslo(pstype, xab, uplw, num_pslo, vowel_cs, suf_way, cus_pre, cus_suf,cus_re, cus_cs, hash_cb, hash_ws, vis_con_cb):
    i = 0
    m = 0
    n = 0
    v = ""
    log.out(0, "Pseudo-localization initialization completed")
    pstr = pstype
    res = ''
    control_txt = False
    if pstr != "" and pstr != "null":
        if uplw == "upper":
            pstr = pstr.upper()
        if uplw == "lower":
            pstr = pstr.lower()
        if xab == "enxa":
            for l in pstr:
                # 基本定义及控制
                i += 1
                if control_txt == True:
                    control_txt = False
                    continue
                # 隐藏控制符
                if vis_con_cb == True:
                    if l == "%" and pstr[i] == "s":
                        control_txt = True
                        continue
                    if l == "\\" and pstr[i] == "n":
                        control_txt = True
                        continue
                    if l == "\\" and pstr[i] == "r":
                        control_txt = True
                        continue
                # 基本字母伪本地化
                al = l.replace('a',random.choice(arra)).replace('A',random.choice(arraa)).replace('b',random.choice(arrb)).replace('B',random.choice(arrbb)).replace('c',random.choice(arrc)).replace('C',random.choice(arrcc)).replace('d',random.choice(arrd)).replace('D',random.choice(arrdd)).replace('e',random.choice(arre)).replace('E',random.choice(arree)).replace('f',random.choice(arrf)).replace('F',random.choice(arrff)).replace('g',random.choice(arrg)).replace('G',random.choice(arrgg)).replace('h',random.choice(arrh)).replace('H',random.choice(arrhh)).replace('i',random.choice(arri)).replace('I',random.choice(arrii)).replace('j',random.choice(arrj)).replace('J',random.choice(arrjj)).replace('k',random.choice(arrk)).replace('K',random.choice(arrkk)).replace('l',random.choice(arrl)).replace('L',random.choice(arrll)).replace('m',random.choice(arrm)).replace('M',random.choice(arrmm)).replace('n',random.choice(arrn)).replace('N',random.choice(arrnn)).replace('o',random.choice(arro)).replace('O',random.choice(arroo)).replace('p',random.choice(arrp)).replace('P',random.choice(arrpp)).replace('q',random.choice(arrq)).replace('Q',random.choice(arrqq)).replace('r',random.choice(arrr)).replace('R',random.choice(arrrr)).replace('s',random.choice(arrs)).replace('S',random.choice(arrss)).replace('t',random.choice(arrt)).replace('T',random.choice(arrtt)).replace('u',random.choice(arru)).replace('U',random.choice(arruu)).replace('v',random.choice(arrv)).replace('V',random.choice(arrvv)).replace('w',random.choice(arrw)).replace('W',random.choice(arrww)).replace('x',random.choice(arrx)).replace('X',random.choice(arrxx)).replace('y',random.choice(arry)).replace('Y',random.choice(arryy)).replace('z',random.choice(arrz)).replace('Z',random.choice(arrzz))
                # 数字伪本地化判断
                if num_pslo == "2":
                    al = l.replace('1',random.choice(arr1)).replace('2',random.choice(arr2)).replace('3',random.choice(arr3)).replace('4',random.choice(arr4)).replace('5',random.choice(arr5)).replace('6',random.choice(arr6)).replace('7',random.choice(arr7)).replace('8',random.choice(arr8)).replace('9',random.choice(arr9)).replace('0',random.choice(arr0))
                elif num_pslo == "1":
                    al = l.replace('1','①').replace('2','②').replace('3','③').replace('4','④').replace('5','⑤').replace('6','⑥').replace('7','⑦').replace('8','⑧').replace('9','⑨')           
                # 元音复重复
                if l.lower() in "aeiou":
                    al = al * (int(vowel_cs) + 1)
                res += al
                log.out(0, "Number of pseudo-localization work cycles: " + str(i))   
        log.out(0, "Digital pseudo-localization program: " + str(num_pslo))
        log.out(0, "Number of vowel repetitions: " + str(vowel_cs))
        if xab == "enxb": # 使用en-XB
            for l in pstr:
                i += 1
            res = pstr[::-1]
        log.out(0, "Pseudo-localization solutions: " + xab+","+uplw)

        # 前后缀添加
        suf = ""
        if suf_way == "1":           
            while i > 2 and n < (i / 7): 
                suf = suf + "!"  
                n += 1
                if n % 3 == 0 & n != int(i / 7+1):
                    suf = suf+" "
            res = "[" +  res + " " + suf + "]";  
        elif suf_way == "2":
            while n < (i / 7):               
                suf = suf + arrba[n % 20]+" "
                n += 1  
            res = "[" + res + " " + suf + "]"
        elif suf_way == "3":
            while n < (i / 3):               
                suf = suf + arrnum[n % 10]
                n += 1  
            res = "[" + res + " " + suf + "]"
        elif suf_way == "4":
            while n < (i / int(cus_cs)):               
                suf = suf + cus_re + " "
                n += 1
            res = cus_pre + res + " " + suf + cus_suf 

        n = 0
        suf = ""
        log.out(0, "Prefix & suffix addition scheme: " + str(suf_way))
            

        # 添加Hash ID
        if hash_cb == True:
            log.out(0, "Add Hash ID: True")
            hash_id = ""
            while m < int(hash_ws):
                hash_id = hash_id + random.choice(arral)               
                m += 1
            log.out(0, "Number of Hash ID bits: " + str(hash_ws))
            res = "[" + hash_id + "]" + res
            hash_id = ""
            m = 0
        else:
            log.out(0, "Add Hash ID: False")
        output = res
        log.out(0, "Result: " + output)
        return output
    log.out(1, "Pseudo-localization completed")
