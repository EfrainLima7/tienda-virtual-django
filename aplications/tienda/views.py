from django.shortcuts import render
from django.views.generic import (
    View,
    ListView,
    DetailView,
)

# local
from .models import Producto
from aplications.categoria.models import Categoria

class Tienda(ListView):
    template_name = 'store/store.html'
    context_object_name ='productos' 
    paginate_by = 3   
    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order",'')
        queryset = Producto.objects.buscar_producto(kword, order)              
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kword = self.request.GET.get("kword", '')
        order = self.request.GET.get("order",'')
        context["total_productos"] = Producto.objects.buscar_producto(kword, order).count()
        context ["categoria"] = Categoria.objects.all()   
        return context
    

class DetalleProducto(DetailView):
    model =Producto
    template_name = "store/product_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #
    #     context["ventas_mes"] = SaleDetail.objects.ventas_mes_producto(
    #         self.kwargs['pk']
    #     )
    #     return context

