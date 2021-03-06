# Generated by Django 2.2.4 on 2020-05-13 18:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=120, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('imagen_referencial', models.ImageField(blank=True, null=True, upload_to='autores/', verbose_name='Imagen Referencial')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoría')),
                ('imagen_referencial', models.ImageField(upload_to='categoria/', verbose_name='Imagen referencial')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('twitter', models.URLField(verbose_name='Twitter')),
            ],
            options={
                'verbose_name': 'Red Sociale',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('correo', models.EmailField(max_length=200, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('nosotros', models.TextField(verbose_name='Nosotros')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('direccion', models.CharField(max_length=200, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Web',
                'verbose_name_plural': 'Webs',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_de_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_de_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de modificacion')),
                ('fecha_de_eliminacion', models.DateField(auto_now=True, verbose_name='Feacha de eliminacion')),
                ('titulo', models.CharField(max_length=150, unique=True, verbose_name='Titulo del Post')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen_referencial', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen Referencial')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado/No publicado')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
