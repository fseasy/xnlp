#!/usr/bin/env python
#coding=utf8

'''
Inspired by code of Oneplus, Zhilong,Deng, 

characters are almostly found from SoGou PinYin IME
'''

special_symbol_ori = [ "△▽○◇□☆▷◁♤♡♢♧▲▼●◆■★▶◀♠♥♦♣☼☽♀☺◐☑√✔☜☝☞㏂☀☾♂☹◑☒×✘☚☟☛㏘█▇▆▅▄▃▂▁…‥•▪∷※░▒▓▏▎▍▌▋▊▉",
                        "♩♪♫♬§〼◎¤۞℗®©㏇™℡〓▬卐卍¶‖♮♯♭☌☍☋☊㉿◮◪◔◕@㈱№♈♉♊♋♌♎♏♐♑♓♒♍",
                        "↖↑↗▨▤▧◤㊤◥☴☲☷☱☯☳㊨㊥㊧▥▦▩→㊣←↙↓↘▫◈▣◣㊦◢☶☵☰‡†▔￢¬⊰⋚⋌⋛⊱↔↕",
                        "*＊✲❈❉✿❀❃❁☸✖✚✄✁✌✍✎₪ி❧❦ღ❤✪☁☂☃☄♨☇☈☡➷⊹✉☏☎ஐ☩➹〄☮☪❂☭☠☣☢✈〠۩✙✟☤☥☦☧☨☫☬♔♚♕♛♗♝♘♞♖♜♙♟"
                        ]

punc_ori = ["，。？！：；、……～＆＠＃",
            ",.?!:;·…~&@#",
            "“”‘’〝〞 \"'＂＇´＇（）【】《》＜＞﹝﹞<>()[]«»‹›〔〕〈〉{}［］「」｛｝〖〗『』", # Attention, has escape `"`
            "︵︷︹︿︽﹁﹃︻︗/|\︶︸︺﹀︾﹂﹄︼︘／｜＼ˊ¨­^¡¦`﹎﹍﹏＿_¯￣﹋﹉﹊ˋ︴¿ˇ　"  , # Attention, has full-width space
            ]

serial_number_ori = [   "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳",
                        "⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇",
                        "⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛",
                        "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ",
                        "❶❷❸❹❺❻❼❽❾❿㈠㈡㈢㈣㈤㈥㈦㈧㈨㈩"
]

math_ori = [ "﹢﹣·/=﹤﹥≦≧≮≯≡＋－×÷＝＜＞≤≥≈≒≠﹢﹣±∶∵∴∷㏒㏑∑∏∅",
             "∝∽∈∩∧⊙⌒∥∟∣∂∆∞≌∉∪∨⊕⊿⊥∠∫∬∭%‰％º¹²³ⁿ℅∮∯∰₁₂₃½⅓⅔¼¾°℃℉〒",
             "㎎㎏μm㎜㎝㎞′¥$€฿￡㎡㎥㏄mlmol㏕″￥£￠₠"
]

pinyin_ori = [ "āáǎàōóǒòêńēéěèīíǐìňūúǔùǖǘǚǜü",
               "ㄚㄛㄜㄧㄨㄩㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙ"
]

digit_ori = [ "零壹贰叁肆伍陆柒捌玖拾佰仟万亿兆",
                      "一二三四五六七八九十百千",
              "0123456789",
              "０１２３４５６７８９０"          
]

letter_ori = [
              "abcdefghijklmnopqrstuvwxyz",
              "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
              "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
              "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
        ]

## for print

name2list = {
    "special symbol" : special_symbol_ori,
    "punctuation" : punc_ori,
    "serial number" : serial_number_ori,
    "mathematic symbol" : math_ori,
    "pinyin" : pinyin_ori,
    "digit" : digit_ori,
    "letter" : letter_ori
}

for name , list in name2list.items() :
    # to single list
    char_list = []
    for l in list :
        unicode_list = l.decode("utf-8")
        char_list.extend(unicode_list)
    # print
    print ("{name}\n"
          "utf-8 char list : \n"
          "{utf8_list}\n"
          "utf-8 char code list : \n"
          "{utf8_code_list}\n").format(name=name, 
                  utf8_list=", ".join(map(lambda x : x.encode("utf-8"), char_list)), 
                  utf8_code_list=", ".join(map( lambda x : repr(x.encode("utf-8")), char_list)))

