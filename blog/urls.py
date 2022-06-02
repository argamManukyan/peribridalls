from django.urls import path
from .views import *

urlpatterns = [
    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug>/', blog_details, name='blog_details'),
    path('blog-category/<slug>/', blog_category, name='blog_category'),
]
