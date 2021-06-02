from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'curso': 'cursinho show',
        'outro': 'o cursinho é massa'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')