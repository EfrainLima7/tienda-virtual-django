from django.shortcuts import render

from django.views.generic import (
    ListView,
)
#local
from aplications.tienda.models import Producto

class Home(ListView):
    template_name = "home.html"
    context_object_name ='productos'
    
    def get_queryset(self):
        queryset = Producto.objects.all().filter(is_available=True).order_by('created_date')
        return queryset