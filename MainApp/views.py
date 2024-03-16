from django.http import Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from MainApp.models import Snippet


def index_page(request):
    print('test1')
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    print('test2')
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    print('test3')
    snipets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов','snipets_dic': snipets}
    return render(request, 'pages/view_snippets.html', context)


def get_snippets_info_page(request,snip_id):
    try:
        get_snip = Snippet.objects.get(pk=snip_id)
        context = {'pagename': get_snip.name, 'snip_id_info': get_snip}
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Snippet with id={snip_id} not found.")
    
    return render(request, 'pages/snippet_info.html', context)
