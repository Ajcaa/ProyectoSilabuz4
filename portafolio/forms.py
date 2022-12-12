from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Para el formulario
from .models import Formdata

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


#Para el formulario
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Formdata
        fields = '__all__'  #Todos los campos definidos en el modelo, se crearan