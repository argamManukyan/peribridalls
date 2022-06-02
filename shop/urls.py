from django.views.decorators.csrf import csrf_exempt
from django.urls import path, re_path

from .views import *

app_name = 'shop'

urlpatterns = [
    path('', csrf_exempt(home_page), name='home_page'),
    path('collection/', products_list, name='product_list'),
    path('collection/<slug>/', product_details, name='product_details'),
    path('brands/', brand_list, name='brand_list'),
    path('categories/', category_list, name='category_list'),
    re_path('brands/(?P<slug>[\w-]+)/', brand_details, name='brand_details'),
    re_path('category/(?P<slug>[\w-]+)/', category_details, name='category_details'),
    re_path('search/', search, name='search'),
    # path('brands/<slug>/', brand_details, name='brand_details'),
    # path('category/<slug>/', category_details, name='category_details'),
    # path('search/', search, name='search'),

]