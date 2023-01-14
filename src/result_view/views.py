from django.shortcuts import render
from django.views import generic
from . models import ResultView
from django.core.paginator import Paginator

# Create your views here.


def product_list(request):
    products = ResultView.objects.all()
    publisher_filter = request.GET.get('publisher_filter')
    year_filter = request.GET.get('year_filter')
    if publisher_filter:
        products = products.filter(publisher__icontains=publisher_filter)
    if year_filter:
        products = products.filter(release_date__startswith=year_filter)
    years = ResultView.objects.values_list('release_date', flat=True).distinct()
    if not year_filter and not publisher_filter:
        paginator = Paginator(products, 20)
        page = request.GET.get('page', 1)
        products = paginator.get_page(page)
        return render(request, 'result_view/collected_data.html', {'products': products, 'years': years, 'year_filter': year_filter, 'publisher_filter': publisher_filter, 'paginator':paginator,'page':page})
    else:
        return render(request, 'result_view/collected_data.html', {'products': products, 'years': years, 'year_filter': year_filter, 'publisher_filter': publisher_filter})
