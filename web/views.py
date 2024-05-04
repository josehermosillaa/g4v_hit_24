from django.shortcuts import render
from .models import Flan

def indice(request):
    #el contexto, es el diccionario donde se envian los datos
    # flanes = Flan.objects.all() #SELECT * FROM FLAN
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)


def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)
    context = {
        'private_flans': private_flans
    }
    return render(request, 'welcome.html', context)
