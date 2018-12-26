#!/usr/bin/env python
#
# Author: BOOK
# Description: A command-line version of Google-translate in Python
# Third-party library: requests
#
import os, platform, sys
import re
import requests
import getopt
import random

doc = '''

    Usage: Typing the word or sentence and press ENTER to get the result.

    Notice: By default, translate from English to Simplified Chinese

    Options:
        :h | :help      show this help document
        :show lang      show current translate mode
        :c src tran     change translate mode to src -> tran
        :cl             clear the screen
        :q | :exit      quit
    
    Supported language (For all supported language, please check in https://cloud.google.com/translate/docs/languages):
        Arabic                  ar
        Chinese (Simplified)    zh-CN
        Chinese (Traditional)   zh-TW
        English                 en
        French                  fr
        German                  de
        Italian                 it
        Japanese                ja
        Korean                  ko
        Latin                   la
        Polish                  pl
        Romanian                ro
        Russian                 ru
        Spanish                 es
        Thai                    th

    Feed back: https://github.com/book987/google-translate/issues

'''
supported_lang = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "ny", "zh-CN", "zh-TW", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "tl", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "iw", "hi", "hmn", "hu", "is", "ig", "id", "ga", "it", "ja", "jw", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ps", "fa", "pl", "pt", "ma", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "cy", "xh", "yi", "yo", "zu"]

indent = ' ' * 3

# TKKptn = re.compile(r'TKK.*var a\\x3d(-*\d+);var b\\x3d(-*\d+);return (-*\d+)\+')
# TKKptn = re.compile(r'TKK='\'(\d+)')

url = r'https://translate.google.cn/translate_a/single?client=gtx&sl=%s&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=0&tsel=0&kc=4&tk=%s&q=%s'
# headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
ss = requests.session()

"""
Google TK
functions: b, getTKK, getTK
"""
def b(a, e):
    """
    Maight be some kinds of encrypt algorithm
    Args:
        a: unknow
        e: unknow
    """
    a = int(a)
    e = str(e)
    d = 0
    while d < len(e) - 2:
        c = ord(e[d + 2])
        c = c - 87 if ord('a') <= c else c
        c = (a & (2**63-1)) >> c if '+' == e[d + 1] else a << c
        a = a + c & 4294967295 if '+' == e[d] else a ^ c
        d += 3
    return int(a)

def getTKK():
    """
    Get value TKK from google translate website source code
    TKK change randomly(?), although this seems can be fixed.
    """
    # TKKinfo = TKKptn.findaul(ss.get(r'https://translate.google.cn/', headers = headers).text)[0]
    response = ss.get(r'https://translate.google.cn/', headers = headers).text
    result = re.findall(r'(TKK.+?\);)',response)[0]
    TKKinfo = re.findall(r"TKK='(.+)';",result)[0]
    # TKKinfo = TKKptn.findall(ss.get(r'https://translate.google.cn/', headers = headers).text)
    # print ("TMP:", ss.get(r'https://translate.google.cn/', headers = headers).text)
    # print ("TKK:", TKKinfo)
    TKK = '%s.%s' % (TKKinfo[-1], str(eval('%s + %s' % (TKKinfo[0], TKKinfo[1]))))
    return str(TKK)

def getTK(a):
    """
    Get value TK
    Paramenters:
        a - the text that waitting to translate
    """
    a = str(a)
    e = getTKK().split('.')
    try:
        h = int(e[0])
    except ValueError:
        h = 0
    g, d, f = [], 0, 0
    for f in range(len(a)):
        c = ord(a[f])
        if 128 > c:
            g.append(c)
        else:
            if 2048 > c:
                g.append(c >> 6 | 192)
            else:
                if 55296 == (c & 64512) and f + 1 < len(a) and 56320 == (a[f + 1] & 64512):
                    f += 1
                    c = 65536 + ((c & 1023) << 10) + a[f] & 1023
                    g.append(c >> 18 | 240)
                    g.append(c >> 12 & 63 | 128)
                else:
                    g.append(c >> 12 | 224)
                    g.append(c >> 6 & 63 | 128)
                    g.append(c & 63 | 128)
    a = h
    for d in g: a = b(a + d, "+-a^+6")
    a = b(a, "+-3^+b+-f")
    try:
        a ^= int(e[1])
    except ValueError:
        a ^= 0
    a = (a & 2147483647) + 2147483648 if 0 > a else a
    a %= 1000000
    return str(a) + '.' + str(a ^ h)


"""
Translater handler
functions: word_handler, sentence_handler, SP_handler
"""
def word_handler(transinfo):
    """
    Get valuable items from the response, compose and return it for displaying
    Args:
        transinfo: response
    """
    out = [indent + transinfo[0][0][0] + '\n']  # most perfect result
    try:  # include type(s) of the word, corresponding explanation and sample sentence
        for x in transinfo[12]:  # type(s) of the word
            out.append(indent*2 + x[0])  # explanation
            out.extend([indent*3 + _[0] + '\n' + str(indent*3 + _[-1] + '\n' if re.findall(r'\w+_\w+_\w*\.\d{3}', _[-1]) == [] else '') for _ in x[1]])  # sample sentence of the corresponding explanation
    except IndexError:
        pass
    except TypeError:
        pass
    try:  # include synonym in all type(s) of the word
        for x in transinfo[1]:  # type(s) of the word
            out.append(indent*2 + x[0])  # explanation (sorted by possibility)
            out.extend([indent*3 + _[0] + indent*3 + ', '.join(_[1]) for _ in x[2]])  # synonyms of the corresponding explanation (sorted by possibility)
        out.append('\n')    
    except IndexError:
        pass
    except TypeError:
        pass
    return out

def sentence_handler(transinfo):
    """
    Get all the translations from the response, compose and return it for displaying
    Args:
        transinfo: response
    """
    out = []
    out.extend([indent + _[0] for _ in transinfo[5][0][2]])  # translation of the sentence (sorted by possibility)
    out.append('\n')
    return out

def sentence_best_handler(transinfo):
    """
    Get all the translations from the response, compose and return it for displaying
    Args:
        transinfo: response
    """
    return transinfo[5][0][2][0][0]

def SP_handler(text):
    """
    Special operation (start with colon) handler
    Args:
        text: input without colon
    Features:
        1. exit translater
        2. help document
        3. show current translate mode
        4. clear the screen
        5. change translate mode
    """
    global srclang, tranlang
    if text in ['q', 'exit']:
        print("\n(interrupt) Exiting translater.")
        sys.exit(0)
    elif text in ['h', 'help']: print(doc)
    elif text == 'show lang': print('\n%s -> %s\n' % (srclang, tranlang))
    elif text == 'cl': os.system("clear") if platform.system() == "Linux" else os.system("cls")
    elif True in [text.startswith(_) for _ in ['c', 'change']]:
        if False not in [_ in supported_lang for _ in text.split()[1:3]]:
            srclang, tranlang = text.split()[1:3]
            print('\n' + indent + 'translate mode change to: %s -> %s\n' % (srclang, tranlang))
        else:
            print('\n' + indent + 'invalid language code: %s\n' % (text.split()[1] if text.split()[1] not in supported_lang else text.split()[2]))
    else: print('invalid operation')

def translater():
    """
    Get input and do right handle in a loop
    Raises:
        requests.exceptions.Timeout
        requests.exceptions.RequestException
        KeyboardInterrupt
    """
    while True:
        try:
            srctext = raw_input(">>> ").strip()
            if srctext.startswith(':'): SP_handler(srctext[1:])
            else:
                transinfo = eval(ss.get(url % (srclang, tranlang, getTK(srctext), srctext), headers = headers, timeout = 5).text.replace('null', 'None').replace('true', 'True').replace('false', 'False'))
                out = sentence_handler(transinfo) if len(srctext.split()) > 1 else word_handler(transinfo)
                for x in out: print(x)
        except requests.exceptions.Timeout:
            print('\n Requests timeout: please check you network')
        except requests.exceptions.RequestException:
            print('\n Requests error: plesse check you network')
        except KeyboardInterrupt:
            print("\n(interrupt) Exiting translater.")
            sys.exit(0)

def translate2(file1, file2, srclang, tranlang, sindex):
    fin = open(file1, 'r' , encoding='utf-8')
    fout = open(file2, 'w' , encoding='utf-8')
    num = 1
    lines = fin.readlines()[sindex:]
    fin.close()
    #proxies = ['123.244.148.2:40609','106.75.164.15:3128','106.75.226.36:808','116.1.11.19:80','60.208.32.201:80']
    for line in lines:
        line = line.strip('\n')
        #transinfo = eval(ss.get(url % (srclang, tranlang, getTK(line), line), headers = headers, timeout = 5, proxies={'http':proxies[1],'https':proxies[1]}).text.replace('null', 'None').replace('true', 'True').replace('false', 'False'))
        transinfo = eval(ss.get(url % (srclang, tranlang, getTK(line), line), headers = headers, timeout = 5 ).text.replace('null', 'None').replace('true', 'True').replace('false', 'False'))
        out = sentence_best_handler(transinfo)
        print("L[%d]:%s" % (num,out))
        num += 1
        fout.write(out+'\n')
    fout.close()
    # proxies = ['1.119.129.2:8080', '115.174.66.148', '113.200.214.164'] 
    # for line in lines:
    #     line = line.strip('\n')
    #     transinfo = eval(ss.get(
    #         url % (srclang, tranlang, getTK(line), line), 
    #         headers = headers, timeout = 5, proxies={'http':random.choice(proxies)}).text.replace('null', 'None').replace('true', 'True').replace('false', 'False'))
    #     out = sentence_best_handler(transinfo)
    #     print("L[%d]:%s" % (num,out))
    #         num += 1
    #         fout.write(out+'\n')

        #for x in out: print(x)

def _usage():
    print("Description:")
    sys.stderr.write('''google translate from srcfile to targetfile.USAGE:
        python gtranslate.py -i inputfile -o outputfile -s srclang -t tranlang
    OPTIONS:
        -i srcl inputfile
        -o outputfile
        -s srclang
        -t tranlang
        -l show languages supported
        -h show help info''')

if __name__ == '__main__':

    opts,args=getopt.getopt(sys.argv[1:],'i:o:s:t:n:lh', ['input=','output=','srclang=', 'tranlang=','startIndex=','h'])

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    srclang = sys.argv[3]
    tranlang = sys.argv[4]
    # inputfile = "./input.txt"
    # outputfile = "./output.txt"
    # srclang = "zh-CN"
    # tranlang = "en"
    sindex = 0

    for o, a in opts:
        if o in ('-h', '--help'):
            _usage();
            sys.exit();
        elif o in ('-i', '--input'):
            inputfile = a
        elif o in ('-o', '--output'):
            outputfile= a
        elif o in ('-s', '--srclang'):
            srclang = a
        elif o in ('-t', '--tranlang'):
            tranlang = a
        elif o in ('-n', '--startIndex'):
            sindex = a
        else:
            _usage();
            sys.exit(0);

    if (len(sys.argv) < 4):
        _usage()
        sys.exit(0)
    translate2(inputfile, outputfile, srclang, tranlang, int(sindex))
    #print('''
    #This is a free script which provide translation through GOOGLE-TRANSLATION.
    #Type :h or :help for more details.
    #''')
    #translater()


