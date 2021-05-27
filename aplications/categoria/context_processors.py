from .models import Categoria

def menu_links_categorias(request):
    links = Categoria.objects.all()
    return dict(links=links)
