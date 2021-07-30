#!/usr/bin/env python
import sys
import os
import json
import time
import datetime

BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(BASEPATH)
sys.path = [BASEPATH] + sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" %(os.path.basename(BASEPATH))



importdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "import")

if not os.path.exists(importdir):
    os.mkdir(importdir)
if not os.listdir(importdir):
    print("No pastes to import..")
    exit()


#from django.core.files import File
from pastebin.models import Paste, Lang

for fn in os.listdir(importdir):
    fp = os.path.join(importdir, fn)
    try:
        jd = json.loads(open(fp).read())
    except:
        jd = None
    if jd is not None:
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(fp))
        print(mtime)
        print(type(mtime))
        if jd['urlrand']:
            print(jd['urlrand'])
            hl = 'text'
            if 'hl' in jd:
                hl = jd['hl']
            lang, created = Lang.objects.get_or_create(code=hl)
            if created:
                lang.save()
            try:
                paste = Paste.objects.all().get(urlid=jd['urlrand'])
            except Paste.DoesNotExist:
                paste = None
            if not paste:
                paste = Paste()
                paste.urlid   = jd['urlrand']
                paste.ip      = jd['ip']
                paste.text    = jd['text']
                paste.lang    = lang
                paste.private = True
                paste.save()
                paste.time    = mtime
                paste.save()
            else:
                print(paste.time)
                print(type(paste.time))
            
"""
    urlid   = models.CharField(max_length=16)
    ip      = models.GenericIPAddressField()
    text    = models.TextField()
    lang    = models.ForeignKey("Lang")
    private = models.BooleanField(default=False)  # Hide paste from public listing



    ext = os.path.splitext(fn)[1][1:].strip().lower()
    if (ext in imgext):
        num = int(ImageModel.objects.all().filter(title="File %s" %(fn)).count())
        if num == 0:
            print("Adding %s..." %(fn))
            with open(fp) as f:
                imf = File(f)
                im = ImageModel(title="File %s" %(fn), image=imf)
                im.save()
        else:
            print("File with title 'File %s' allready exists, skipping." %(fn))
"""
