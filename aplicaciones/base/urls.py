from django.urls import path
from .views import Inicio, Listado, FormularioContacto, DetallePost, Buscador

urlpatterns = [
    path('', Inicio.as_view(), name='index'),
    path('peliculas/', Listado.as_view(),
         {'nombre_categoria': 'pelicula'}, name='pelicula'),
    path('libros/', Listado.as_view(),
         {'nombre_categoria': 'libros'}, name='libros'),
    path('musica/', Listado.as_view(),
         {'nombre_categoria': 'musica'}, name='musica'),
    path('entrevistas/', Listado.as_view(),
         {'nombre_categoria': 'entrevistas'}, name='entrevistas'),
    path('formulario_contacto/', FormularioContacto.as_view(),
         name='formulario_contacto'),
    path('<slug:slug>/', DetallePost.as_view(),
         name='detalle_post'),
    path('resultados/', Buscador.as_view(),
         name='buscar'),
]
