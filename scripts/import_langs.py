#!/usr/bin/env python2
import sys
import os

BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path = [BASEPATH] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" %(os.path.basename(BASEPATH))



source_types = {
    "text"   : "Plain text",
    "py"     : "Python",
    "pytb"   : "Python Traceback",
    "pycon"  : "Python Console",
    "html"   : "HTML",
    "xml"    : "XML",
    "css"    : "CSS",
    "js"     : "Javascript",
    "bash"   : "Bash",
    "bat"    : "Batch",
    "irc"    : "IRC Logs",
    "php"    : "PHP",
    "perl"   : "Perl",
    "c"      : "C",
    "nasm"   : "NASM",
    "vb.net" : "VB.NET",
    "bf"     : "Brainf**k",
    "java"   : "Java",
    "cl"     : "Common Lisp",
    "diff"   : "Diff",
    "lua"    : "Lua",
    "cpp"    : "C++",
    "yaml"   : "YAML",
}


from pastebin.models import Lang

for hl in source_types:
    lang, created = Lang.objects.get_or_create(code=hl)
    lang.name = source_types[hl]
    lang.save()
