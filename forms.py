from django import forms
from pastebin.models import Lang

class PasteForm(forms.Form):
    private = forms.BooleanField(initial=False, required=False)
    lang = forms.ModelChoiceField(queryset=Lang.objects.all().order_by('-promote', 'name'), empty_label="-----", initial=Lang.objects.get(code='text'))
    text = forms.CharField ( widget=forms.widgets.Textarea() )
    

