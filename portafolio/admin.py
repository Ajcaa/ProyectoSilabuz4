from django.contrib import admin
from .models import Formdata



# Register your models here.
class FormAdmin(admin.ModelAdmin):
    pass



admin.site.register(Formdata)  