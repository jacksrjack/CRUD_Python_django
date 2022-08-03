from django.shortcuts import render, redirect
#from jmespath import search
from serie.forms import SerieForm
from serie.models import Serie
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    data = {}

    search = request.GET.get('q')
    if search:
        all = Serie.objects.filter(nome__icontains=search)
    else:
        all = Serie.objects.all()
    paginacao = Paginator(all, 4)
    pages = request.GET.get('pagina')
    data['db'] = paginacao.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = SerieForm()
    return render(request, 'form.html', data)

def create(request):
    form = SerieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Serie.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Serie.objects.get(pk=pk)
    data['form'] = SerieForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Serie.objects.get(pk=pk)
    form = SerieForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Serie.objects.get(pk=pk)
    db.delete()
    return redirect(home)