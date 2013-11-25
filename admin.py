from django.contrib import admin
from pastebin.models import Paste, Lang

#    urlid   = models.CharField(max_length=16, unique=True)
#    ip      = models.GenericIPAddressField()
#    text    = models.TextField()
#    lang    = models.ForeignKey("Lang")
#    private = models.BooleanField(default=False)  # Hide paste from public listing
#    time    = models.DateTimeField(auto_now_add=True)
class PasteAdmin(admin.ModelAdmin):
    list_display = ('urlid', 'ip', 'lang', 'private', 'time')
    list_filter = ['private', 'time', 'lang']
    search_fields = ['ip', 'text']
    ordering = ['-time']
    date_hierarchy = 'time'



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



admin.site.register(Paste, PasteAdmin)
admin.site.register(Lang, LangAdmin)

