# Generated by Django 2.2.4 on 2020-05-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='etiqueta',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Etiqueta'),
        ),
    ]
