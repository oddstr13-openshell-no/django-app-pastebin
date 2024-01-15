#!/usr/bin/env python
import os
import json

from django.core.management.base import BaseCommand, CommandError

from pastebin.models import Paste

"""
class Paste(models.Model):
    urlid   = models.CharField(max_length=16, unique=True)
    ip      = models.GenericIPAddressField()
    text    = models.TextField()
    lang    = models.ForeignKey("Lang", on_delete=models.PROTECT)
    private = models.BooleanField(default=False)  # Hide paste from public listing
    time    = models.DateTimeField(auto_now_add=True)
    replyto = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="replies") #, related_query_name="reply") # related_query_name requires 1.6

class Lang(models.Model):
    name    = models.CharField(max_length=16, blank=True)  # Display name
    code    = models.CharField(max_length=16, unique=True) # Pygments code
    promote = models.BooleanField(default=False)           # List on the top / commonly used
"""

OUTPUT = os.path.join("dump", "pastebin")


class Command(BaseCommand):
    help = "Dumps paste entries"

    def handle(self, *args, **options):
        if not os.path.exists(OUTPUT):
            os.makedirs(OUTPUT)

        for p in Paste.objects.all():
            with open(os.path.join(OUTPUT, p.urlid) + ".json", "w") as fh:
                json.dump(
                    {
                        "id": p.urlid,
                        "ip": str(p.ip),
                        "content": p.text,
                        "lang": p.lang.code,
                        "private": p.private,
                        "posted": p.time.isoformat(" "),
                        "parent": p.replyto.urlid if p.replyto else None,
                    },
                    fh,
                )
