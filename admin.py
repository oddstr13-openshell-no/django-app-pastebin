from django.contrib import admin
from pastebin.models import Paste, Lang, Ban

#    urlid   = models.CharField(max_length=16, unique=True)
#    ip      = models.GenericIPAddressField()
#    text    = models.TextField()
#    lang    = models.ForeignKey("Lang")
#    private = models.BooleanField(default=False)  # Hide paste from public listing
#    time    = models.DateTimeField(auto_now_add=True)
def ban_ip(modeladmin, request, queryset):
    for p in queryset:
        try:
            ban = Ban.objects.get(ip=p.ip)
        except Ban.DoesNotExist:
            ban = Ban(ip=p.ip)
            ban.save()
ban_ip.short_description = "Ban IP Addresses"

class PasteAdmin(admin.ModelAdmin):
    list_display = ('urlid', 'ip', 'lang', 'private', 'time')
    list_filter = ['private', 'time', 'lang']
    search_fields = ['ip', 'text']
    ordering = ['-time']
    date_hierarchy = 'time'
    actions = [ban_ip]

def enable_promote(modeladmin, request, queryset):
    for p in queryset:
        p.promote = True
        p.save()
enable_promote.short_description = "Promote"

def disable_promote(modeladmin, request, queryset):
    for p in queryset:
        p.promote = False
        p.save()
disable_promote.short_description = "Un-Promote"

class LangAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'promote')
    ordering = ['-promote', 'name']
    actions = [enable_promote, disable_promote]

class BanAdmin(admin.ModelAdmin):
    list_display = ('ip', 'reason', 'time', 'end', 'hits')
    list_filter = ['reason', 'time', 'end']
    search_fields = ['ip', 'reason']
    ordering = ['-time']
    date_hierarchy = 'time'


admin.site.register(Paste, PasteAdmin)
admin.site.register(Lang, LangAdmin)
admin.site.register(Ban, BanAdmin)

