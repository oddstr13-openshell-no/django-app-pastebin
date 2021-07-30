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
from pygments.lexer import RegexLexer
from pygments.formatters import HtmlFormatter
from pygments import token


class ShurtleLexer(RegexLexer):
    # by Cruor
    name = "Shurtle"
    aliases = ["shurtle"]
    filenames = ["*.g"]

    tokens = {
        "root": [
            (r"\d+", token.Literal.Number),
            (r"0x[0-9a-fA-F]+", token.Literal.Number.Hex),
            (r"\d+\.?\d*", token.Literal.Number),
            (r"[\-]?\d+\.?\d*", token.Literal.Number),
            (r"[\-]?\d+\.?\d*[eE][\+\-]?\d+", token.Literal.Number),
            (r"\d+\.?\d*[eE][\+\-]?\d+", token.Literal.Number),

            (r"'.*?'", token.Literal.String),

            (r"\s+", token.Comment),

            (r"[A-Z]", token.Name.Variable),

            (r".", token.Operator)
        ]
    }

LOCAL_LEXERS = {
    'shurtle': ShurtleLexer(),
}

def getLexer(lang):
    lexer = LOCAL_LEXERS.get(lang, None)
    if lexer is not None:
        return lexer

    try:
        return get_lexer_by_name(lang)
    except:
        return get_lexer_by_name("text")

def pygmentize(value, lang="text"):
    lexer = getLexer(lang)
    formatter = HtmlFormatter(cssclass="source")
    return highlight(value, lexer, formatter)
