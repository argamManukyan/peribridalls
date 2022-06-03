from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin
from singlemodeladmin import SingleModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import AboutUs, AboutUsHomepage, OurAdvantages, AboutUsBanner


@admin.register(AboutUs)
class AboutUsAdmin(SingleModelAdmin, TabbedDjangoJqueryTranslationAdmin):
    pass


@admin.register(AboutUsHomepage)
class AboutUsHomepageAdmin(SingleModelAdmin, TabbedDjangoJqueryTranslationAdmin):
    pass


@admin.register(OurAdvantages)
class OurAdvantagesAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):

    def get_icon(self, obj):
        if obj.icon:
            return mark_safe('<img src="{}" width="120px" height="120px" />'.format(obj.icon.url))
        return ''

    get_icon.short_description = 'Նկար'

    list_display = ['name', 'get_icon']


@admin.register(AboutUsBanner)
class AboutUsBannerAdmin(SingleModelAdmin, TabbedDjangoJqueryTranslationAdmin):

    def get_image(self, obj: AboutUsBanner):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" height="300px" width="500px" />')
        return ''

    get_image.short_description = "Բանների նկար"

    readonly_fields = ['get_image']

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj=None)
        fields.insert(1, 'get_image')
        return fields
