from django.shortcuts import render
from .forms import CidadaoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cidadao(request):
    form = CidadaoForm()
    context = {
        'form': form
    }
    return render(request, 'cidadao.html', context)