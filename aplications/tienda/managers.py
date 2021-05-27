# python
from datetime import timedelta
# django
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

class ProductoManager(models.Manager):
    """ procedimiento modelo  """

    def buscar_producto(self, kword, order):
        consulta = self.filter(
            is_available=True
        ).filter(
            Q(nombre_producto__icontains=kword) | Q(descripcion__icontains=kword)| Q (categoria__nombre_categoria=kword)
                        
                
        ) .order_by('-created_date')
        # verificamos en que orden se solicita
        if order == 'polos':
            # ordenar por fecha
            return consulta.order_by('categoria_id')
        elif order == 'name':
            # ordenar por nombre
            return consulta.order_by('nombre_producto')        
        else:
            return consulta.order_by('-created_date')

