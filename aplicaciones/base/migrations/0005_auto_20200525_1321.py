# Generated by Django 2.2.4 on 2020-05-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200523_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen_1',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 1'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_2',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 2'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_3',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 3'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_4',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 4'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_5',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 5'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_6',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 6'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_7',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 7'),
        ),
        migrations.AddField(
            model_name='post',
            name='imagen_8',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='imagenes/', verbose_name='Imagen 8'),
        ),
    ]
