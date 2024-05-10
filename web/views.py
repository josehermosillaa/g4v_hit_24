from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Flan, ContactForm
from .forms import ContactFormForm, ContactFormModelForm


def indice(request):
    #el contexto, es el diccionario donde se envian los datos
    # flanes = Flan.objects.all() #SELECT * FROM FLAN WHERE is_private=False
    public_flans = Flan.objects.filter(is_private=False)
    context = {
        'public_flans':public_flans
    }
    return render(request, 'index.html', context)


def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True) #ORM Django Flan(tabla) objects filter, is_private=true
    #SELECT * FROM FLan WHERE is_private=True
    context = {
        'private_flans': private_flans
    }
    return render(request, 'welcome.html', context)


def contacto(request):
    #el contexto, es el diccionario donde se envian los datos
    # flanes = Flan.objects.all() #SELECT * FROM FLAN WHERE is_private=False
    print(request.POST)
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        #chequear que los datos son validos
        if form.is_valid():
            #procesamos los datos del formulario
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
    else:
        #si entro por la url (method GET)
        # form = ContactFormForm()
        form = ContactFormModelForm()
    context = {'form':form}
    return render(request, 'contact.html', context)

    
def exito(request):
    return render(request, 'exito.html')


def receta(request, flan_uuid):
    flan = Flan.objects.get(flan_uuid = flan_uuid)
    context = {'flan': flan}
    return render(request, 'receta.html', context)

class MiVistaProtegida(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'