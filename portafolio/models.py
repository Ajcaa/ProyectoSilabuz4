from django.db import models

# Create your models here.


class Formdata(models.Model):
    photo = models.URLField(verbose_name='Foto (URL)')
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.CharField(max_length=100, verbose_name='Descripcion')
    tags = models.CharField(max_length=100, verbose_name='Tags')
    url_github = models.URLField(verbose_name='Github (URL)')

class IPdata(models.Model):
    ip = models.CharField(max_length=100)