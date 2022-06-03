from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static, settings

import shop.views
from wish.views import add_to_wish

admin.site.site_header = 'Peri Bridals'                    # default: "Django Administration"
admin.site.index_title = 'Peri Bridals'                 # default: "Site administration"
admin.site.site_title = 'Peri Bridals'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('add_to_wish/', add_to_wish, name='add_to_wish'),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('index/faq/', include('faq.urls')),
    path('index/contact-us/', include('contactus.urls')),
    path('index/peri-tv/', include('videos.urls')),
    path('index/', include('blog.urls')),
    path('index/', include('shop.urls', namespace='shop')),
    path('index/', include('about.urls')),
    path('index/', include('wish.urls')),
    path('index/', include('gallery.urls')),
    path('index/', include('staticpages.urls')),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
