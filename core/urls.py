from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

import shop.views
from wish.views import add_to_wish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_to_wish/', add_to_wish, name='add_to_wish'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('rosetta/', include('rosetta.urls')),
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
