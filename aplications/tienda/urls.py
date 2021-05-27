from django.urls import path
from . import views

app_name = "store_app"
urlpatterns = [
    path('tienda/', views.Tienda.as_view(), name='tienda'),
    path('tienda/dtail/<slug>', views.DetalleProducto.as_view(), name='detalle_producto'),
]
