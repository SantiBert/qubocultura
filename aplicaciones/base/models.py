from django.db import models
from ckeditor.fields import RichTextField


class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_de_creacion = models.DateField(
        'Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_de_modificacion = models.DateField(
        'Fecha de modificacion', auto_now=True, auto_now_add=False)
    fecha_de_eliminacion = models.DateField(
        'Feacha de eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Categoria(ModeloBase):
    nombre = models.CharField('Nombre de la categoría',
                              max_length=100, unique=True)
    etiqueta = models.CharField(
        'Etiqueta', max_length=100, null=True, blank=True)
    imagen_referencial = models.ImageField(
        'Imagen referencial', upload_to='categoria/')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre


class Autor(ModeloBase):
    nombre = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=120)
    email = models.EmailField('E-mail', max_length=200, null=True, blank=True)
    imagen_referencial = models.ImageField(
        'Imagen Referencial', upload_to='autores/', null=True, blank=True)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombre)


class Post(ModeloBase):
    titulo = models.CharField('Titulo del Post', max_length=150, unique=True)
    slug = models.CharField('Slug', max_length=150, unique=True)
    descripcion = models.TextField('Descripción')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    contenido = RichTextField()
    imagen_referencial = models.ImageField(
        'Imagen Referencial', upload_to='imagenes/', max_length=255)
    publicado = models.BooleanField('Publicado/No publicado', default=False)
    destacado = models.BooleanField('Destacado/No destacado', default=False)
    fecha_publicacion = models.DateField('Fecha de publicación')
    imagen_1 = models.ImageField(
        'Imagen 1', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_2 = models.ImageField(
        'Imagen 2', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_3 = models.ImageField(
        'Imagen 3', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_4 = models.ImageField(
        'Imagen 4', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_5 = models.ImageField(
        'Imagen 5', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_6 = models.ImageField(
        'Imagen 6', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_7 = models.ImageField(
        'Imagen 7', upload_to='imagenes/', max_length=255, null=True, blank=True)
    imagen_8 = models.ImageField(
        'Imagen 8', upload_to='imagenes/', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
<<<<<<< HEAD
        ordering = ['-fecha_publicacion']
=======
        ordering = ['-fecha_de_creacion']
>>>>>>> faccff3d2e4aaaa3a7bf91f10e0eefe13563fa5a

    def __str__(self):
        return self.titulo


class Web(ModeloBase):
    nosotros = models.TextField('Nosotros')
    telefono = models.CharField('Telefono', max_length=10)
    email = models.EmailField('E-mail', max_length=200)
    direccion = models.CharField('Direccion', max_length=200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'

    def __str__(self):
        return self.nosotros


class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    instagram = models.URLField('Instagram')
    twitter = models.URLField('Twitter')

    class Meta:
        verbose_name = 'Red Sociale'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.facebook


class Contacto(ModeloBase):
    nombre = models.CharField('Nombres', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=150)
    correo = models.EmailField('E-mail', max_length=200)
    asunto = models.CharField('Asunto', max_length=100)
    mensaje = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.asunto


class Suscriptor(ModeloBase):
    correo = models.EmailField('E-mail', max_length=200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.correo
