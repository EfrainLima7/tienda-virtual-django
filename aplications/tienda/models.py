from django.db import models
from aplications.categoria.models import Categoria

# Create your models here.
from .managers import ProductoManager

class Producto(models.Model):
    nombre_producto    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    descripcion     = models.TextField(max_length=500, blank=True)
    precio           = models.IntegerField()
    images          = models.ImageField(upload_to='fotos/productos')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    categoria        = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    objects = ProductoManager()
    def __str__(self):
        return self.nombre_producto