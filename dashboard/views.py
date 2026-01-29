from django.shortcuts import render
from django.core.paginator import Paginator
from .data import get_analytics_data


def dashboard(request):
    """
    Vista principal del Portal Analítico.
    
    Renderiza la página principal con datos simulados de analítica.
    Implementa paginación de 5 registros por página.
    
    Args:
        request: Objeto HttpRequest de Django.
        
    Returns:
        HttpResponse: Página HTML del dashboard con los datos paginados.
    """

    analytics_data = get_analytics_data()
    paginator = Paginator(analytics_data, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'title': 'Analytics Portal',
        'analytics_data': page_obj.object_list,
        'page_obj': page_obj,
        'paginator': paginator,
    }
    return render(request, 'dashboard/index.html', context)
