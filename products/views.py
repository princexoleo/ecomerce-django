from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product,ProductManager

# Create your views here.
# class based view Featured
class ProductFeaturedListView(ListView):
    #queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args,**kwargs):
    #     context = super(ProductListView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()


# Featured DetailView-class based
class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = 'products/featured_detail.html'

    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return Product.objects.featured()


#function based Product listview
def product_list_view(request):
    queryset = Product.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request,'products/list.html', context)





# class based
class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_context_data(self, *args,**kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        return context
    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()
    


#function based listview
def product_list_view(request):
    queryset = Product.objects.all()
    context ={
        'object_list': queryset
    }
    return render(request,'products/list.html', context)

# slug view of product
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'


#DetailView-class based
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    # with the help of model Manager
    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product,slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404(" Not Found !")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = instance.first()
        except:
            raise Http404("Uhhmm !") 
        return instance

    def get_context_data(self, *args,**kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        return context
    
    # with the help of model Manager
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(id=pk)
        print(instance)
        if instance is None:
            raise Http404("Product Doesn't exists!!")
        return instance
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)
    


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
    instance = Product.objects.get_by_id(id=pk)
    print(instance)
    if instance is None:
        raise Http404("Product Doesn't exists!!")
    context['object'] = instance
    #qs = Product.objects.filter(id=pk)
    
    # if qs.exists() and qs.count() ==1:
    #     instance = qs.first()
    #     context['object'] = instance
    # else:
    #     raise Http404("Product doesn't exists!")
    return render(request,'products/detail.html', context)

