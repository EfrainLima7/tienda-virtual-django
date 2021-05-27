from django.db import models
from django.urls import reverse

# Create your models here.
from aplications.tienda.managers import ProductoManager

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='fotos/categoria', blank=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias '

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.nombre_categoria