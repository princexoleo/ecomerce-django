from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product

# Create your views here.
# class based view 
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args,**kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        return context
    


#function based listview
def product_list_view(request):
    queryset = Product.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request,'products/list.html', context)


#DetailView
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args,**kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context
    


#function based listview
def product_detail_view(request, pk=None,*args, **kwargs):
    #instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    context ={
        'object': ""
    }
    # try:
    #     instance = Product.objects.get(id=pk)
    #     context['object'] = instance
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product Doesnot Exists")
    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() ==1:
        instance = qs.first()
        context['object'] = instance
    else:
        raise Http404("Product doesn't exists!")
    return render(request,'products/detail.html', context)

