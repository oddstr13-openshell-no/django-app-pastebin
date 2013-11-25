from time import time as time_t
from random import randint
from base64 import b64encode

def n2b(n):
    res = ""
    while n:
        c = chr(n & 0xff)
        res = c + res
        n >>= 8
    return res

def genUrlid():
    b = n2b(int(time_t())) + n2b(randint(0x0000,0xffff))
    res = b64encode(b, "-_").strip("=")
    return res


from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def pygmentize(value, lang="text"):
    try:
        lexer = get_lexer_by_name(lang)
    except:
        lexer = get_lexer_by_name("text")
    formatter = HtmlFormatter(cssclass="source")
    return highlight(value, lexer, formatter)
