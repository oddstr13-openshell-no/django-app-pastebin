from django.db import models

class Paste(models.Model):
    urlid   = models.CharField(max_length=16, unique=True)
    ip      = models.GenericIPAddressField()
    text    = models.TextField()
    lang    = models.ForeignKey("Lang", on_delete=models.PROTECT)
    private = models.BooleanField(default=False)  # Hide paste from public listing
    time    = models.DateTimeField(auto_now_add=True)
    replyto = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="replies") #, related_query_name="reply") # related_query_name requires 1.6

    def __unicode__(self):
        return self.urlid

class Lang(models.Model):
    name    = models.CharField(max_length=16, blank=True)  # Display name
    code    = models.CharField(max_length=16, unique=True) # Pygments code
    promote = models.BooleanField(default=False)           # List on the top / commonly used

    def __unicode__(self):
        return self.name or self.code
