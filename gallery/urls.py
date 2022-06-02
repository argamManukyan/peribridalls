from django.urls import path

from .views import gallery_list, gallery_details

urlpatterns = [
    path('gallery/', gallery_list, name='gallery_list'),
    path('gallery/<slug>/', gallery_details, name='gallery_details'),

]