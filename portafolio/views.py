from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from portafolio.forms import CustomUserCreationForm

#Para el formulario
from .forms import PortfolioForm
from django.urls import reverse

#Para visualizar el portafolio
from .models import Formdata


# Create your views here.
def home(request):
    return render(request, 'entry/home.html')

def welcome(request):
    projects = Formdata.objects.all()
    return render(request, 'entry/index.html',{'projects': projects})


@login_required
def form(request):
    fill_form = PortfolioForm()

    if request.method == 'POST':
        contact_form = PortfolioForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            # Tengo que avisar que todo fue bien
            return redirect(reverse('form')+'?ok')  #form.html
        
        else:
            #Tengo que generar un error
            return redirect(reverse('form')+'?error')      


    return render(request, 'entry/form.html', {'formu': fill_form}) #para pasarlo a la vista como contexto




def exit(request):
    logout(request)
    return redirect('home')






def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')

    return render(request, 'registration/register.html', data)





