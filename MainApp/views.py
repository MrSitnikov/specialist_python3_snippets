from django.http import Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponse
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form':form}
        return render(request, 'pages/add_snippet.html', context)
    else:
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets_page")
        return render(request, 'add_snippet.html', {'form': form})


def deleteSnippet(request, snip_id):
    #student = get_object_or_404(Student, id=id)
    if request.method == 'GET':
        get_snip = Snippet.objects.get(pk=snip_id)
        get_snip.delete()
        return redirect('snippets_page')
    return render(request, 'pages/view_snippets.html', snippets_page)

def update_snippet_page(request, snip_id):
    get_snip = Snippet.objects.get(pk=snip_id)
    if request.method == 'GET':
        
        form = SnippetForm(instance=get_snip)
        return render(request, 'pages/add_snippet.html', {'form': form})
    if request.method == "POST":
        data_form = request.POST
        get_snip.name = data_form["name"]
        get_snip.code = data_form["code"]
        if (change_date := data_form.get("creation_date")):
            get_snip.creation_date = change_date
        get_snip.save()
        return redirect("snippets-list")

    
    
# def create_snippet(request):
#    if request.method == "POST":
#        form = SnippetForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("snippets_page")
#        return render(request, 'add_snippet.html', {'form': form})


def snippets_page(request):
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


def login(request):
   if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username =", username)
        # print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
        else:
            pass
        return redirect('home')

def logout(request):
    auth.logout(request)
    return redirect('home')

def registration(request):
    print(request.method)
    if request.method == "GET":
        form = UserRegistrationForm()
        print(form.as_p)
        context = {
            'pagename': 'Регистрация',
            'form':form}
        return render(request, 'pages/register.html', context)
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, 'pages/register.html', {'form': form})
