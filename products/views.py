from django.views import ListView
from django.shortcuts import render

from .models import Product

# Create your views here.
# class based view 
class ProductListView(ListView):
    queryset = Product.objects.all()
    


#function based listview
def product_list_view(request):
    queryset = Product.objects.all()
    context =[
        'objects_list':queryset,
    ]
    return render(request,'product/product_list_view.html', context)
