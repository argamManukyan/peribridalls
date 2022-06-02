from django.contrib import admin
# from adminsortable2.admin import
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin

from .models import Header, Slider


@admin.register(Header)
class HeaderAdmin(TabbedDjangoJqueryTranslationAdmin):
    pass


@admin.register(Slider)
class SliderAdmin(TabbedDjangoJqueryTranslationAdmin):

    def get_xl_image(self, instance: Slider):
        return mark_safe('<img src="{}" height="120px" width="120px" />'.format(instance.image.url))

    get_xl_image.short_description = 'Նկար'

    list_display = ['get_xl_image']