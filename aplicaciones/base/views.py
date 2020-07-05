import random
from django.shortcuts import render, redirect
from django.views.generic import ListView, View, DetailView
from django.core.mail import send_mail
from qultura.configuracion.base import EMAIL_HOST_USER
from .models import Post, Categoria, RedesSociales, Web, Suscriptor
from .utils import consulta, obtenerRedes, obtenerWeb, generarCategoria
from .forms import ContactoForm
from django.shortcuts import get_object_or_404
from django.db.models import Q


class Inicio(ListView):
    def get(self, request, *args, **kwargs):
        posts = list(Post.objects.filter(
            estado=True,
            publicado=True
        ).values_list('id', flat=True))

        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        # Ramdamizador de post por categoria
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        # Ultimo post de cada categoria
        try:
            post_libros = Post.objects.filter(
                estado=True,
                publicado=True,
                categoria=Categoria.objects.get(nombre='libros')
            ).latest('fecha_publicacion')
        except:
            post_libros = None

        try:
            post_pelicula = Post.objects.filter(
                estado=True,
                publicado=True,
                categoria=Categoria.objects.get(nombre='pelicula')
            ).latest('fecha_publicacion')
        except:
            post_pelicula = None

        try:
            post_musica = Post.objects.filter(
                estado=True,
                publicado=True,
                categoria=Categoria.objects.get(nombre='musica')
            ).latest('fecha_publicacion')
        except:
            post_musica = None

        try:
            post_entrevistas = Post.objects.filter(
                estado=True,
                publicado=True,
                categoria=Categoria.objects.get(nombre='entrevistas')
            ).latest('fecha_publicacion')
        except:
            post_entrevistas = None

        contexto = {
            'principal': principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_libros': post_libros,
            'post_pelicula': post_pelicula,
            'post_musica': post_musica,
            'post_entrevistas': post_entrevistas,
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
        }

        return render(request, 'index.html', contexto)


class Listado(ListView):
    def get(self, request, nombre_categoria, *args, **kwargs):
        contexto = generarCategoria(request, nombre_categoria)
        return render(request, 'categoria.html', contexto)


class FormularioContacto(View):
    def get(self, request, *args, **kwargs):
        form = ContactoForm()
        contexto = {
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
            'form': form,
        }
        return render(request, 'contacto.html', contexto)

    def post(self, request, *args, **kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base:index')
        else:
            contexto = {
                'form': form,
            }
            return render(request, 'contacto.html', contexto)


class DetallePost(DetailView):
    def get(self, request, slug, *args, **kwargs):
        try:
            post = Post.objects.get(slug=slug)
        except:
            post = None

        posts = list(Post.objects.filter(
            estado=True,
            publicado=True
        ).values_list('id', flat=True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        contexto = {
            'post': post,
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
        }
        return render(request, 'post.html', contexto)


class Buscador(View):
    def post(self, request, *args, **kwargs):
        queryset = request.POST.get("buscar")
        if queryset:
            posts = Post.objects.filter(
                Q(titulo__icontains=queryset) |
                Q(contenido__icontains=queryset),
                estado=True,
                publicado=True
            ).distinct()

        return render(request, 'resultado.html', {'posts': posts})


