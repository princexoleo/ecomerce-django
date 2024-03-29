"""ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ecomerce import views

from products.views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    product_detail_view,
    ProductDetailSlugView,
    ProductFeaturedListView,
    ProductFeaturedDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page),
    path('about/',views.about_page),
    path('contact/',views.contact_page),
    path('login/',views.login_page),
    path('register/',views.register_page),
    path('products/',ProductListView.as_view()),
    path('featured/',ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/',ProductFeaturedDetailView.as_view()),
    path('products_list/',product_list_view),
    #path('products/<int:pk>/',ProductDetailView.as_view()),
    path('products/<slug:slug>/',ProductDetailSlugView.as_view()),
    path('products_list/<int:pk>/',product_detail_view),
    
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
