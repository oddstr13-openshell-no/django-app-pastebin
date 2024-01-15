#!/usr/bin/env python2
from django import template
from django.utils.safestring import mark_safe

import genshi

from pastebin.lib import pygmentize as _hl

register = template.Library()


@register.filter(name="pygmentize", is_safe=True)
def pygmentize(value, lang="text"):
    return mark_safe(genshi.Markup(_hl(value, lang=lang)))
