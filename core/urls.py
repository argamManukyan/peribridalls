from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static, settings
from wish.views import add_to_wish

admin.site.site_header = 'Peri Bridals'  # default: "Django Administration"
admin.site.index_title = 'Peri Bridals'  # default: "Site administration"
admin.site.site_title = 'Peri Bridals'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('add_to_wish/', add_to_wish, name='add_to_wish'),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('faq/', include('faq.urls')),
    path('contact-us/', include('contactus.urls')),
    path('peri-tv/', include('videos.urls')),
    path('', include('blog.urls')),
    path('', include('shop.urls', namespace='shop')),
    path('', include('about.urls')),
    path('', include('wish.urls')),
    path('', include('gallery.urls')),
    path('', include('staticpages.urls')),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'shop.views.page_not_found_view'
handler500 = 'shop.views.server_error_view'
