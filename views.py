from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from sys import stdout

from pastebin.models import Paste, Lang
from pastebin.forms import PasteForm
from pastebin.lib import genUrlid


def show(request, urlid):
    paste = get_object_or_404(Paste, urlid=urlid)
    return render(request, 'show.html', {'paste':paste})

def showraw(request, urlid):
    paste = get_object_or_404(Paste, urlid=urlid)
    return HttpResponse(paste.text)

def index(request):
    f = PasteForm()
    pastes = Paste.objects.all().filter(private=False).order_by('-time')[:100]
    return render(request, 'index.html', {'pastes':pastes,'form':f})

@csrf_exempt
def create(request):
    if request.method == 'POST':
        f = PasteForm(request.POST)
        if f.is_valid():
            p = Paste()
            p.private = f.cleaned_data['private']
            p.text = f.cleaned_data['text']
            p.lang = f.cleaned_data['lang']
            p.urlid = genUrlid()
            p.ip = request.META.get('REMOTE_ADDR')
            p.save()
            return HttpResponseRedirect('/paste/' + p.urlid)
    else:
        f = PasteForm()
    return render(request, 'create.html', {'form':f})

@csrf_exempt
def reply(request, urlid):
    replyto = get_object_or_404(Paste, urlid=urlid)
    if request.method == 'POST':
        f = PasteForm(request.POST)
        if f.is_valid():
            p = Paste()
            p.private = f.cleaned_data['private']
            p.text = f.cleaned_data['text']
            p.lang = f.cleaned_data['lang']
            p.urlid = genUrlid()
            p.ip = request.META.get('REMOTE_ADDR')
            p.replyto = replyto
            p.save()
            return HttpResponseRedirect('/paste/' + p.urlid)
    else:
        f = PasteForm(initial={
          'private' : replyto.private,
          'text'    : replyto.text,
          'lang'    : replyto.lang,
        })
    return render(request, 'reply.html', {
      'form'  : f,
      'reply' : replyto,
      })

