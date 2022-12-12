# Generated by Django 4.1.4 on 2022-12-10 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.URLField(verbose_name='Foto (URL)')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('tags', models.CharField(max_length=100, verbose_name='Tags')),
                ('url_github', models.URLField(verbose_name='Github (URL)')),
            ],
        ),
    ]