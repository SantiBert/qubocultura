from django.urls import path
from .views import Inicio, Listado, FormularioContacto, DetallePost, Buscador

urlpatterns = [
<<<<<<< HEAD
=======
     path('resultados/', Buscador.as_view(),
         name="buscar"),    
>>>>>>> faccff3d2e4aaaa3a7bf91f10e0eefe13563fa5a
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
<<<<<<< HEAD
    path('<slug:slug>/', DetallePost.as_view(),
         name='detalle_post'),
    path('resultados/', Buscador.as_view(),
         name='buscar'),
=======
     
    path('<slug:slug>/', DetallePost.as_view(),
         name='detalle_post'),

>>>>>>> faccff3d2e4aaaa3a7bf91f10e0eefe13563fa5a
]
