from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin

from blog.models import Blog, BlogCategory


@admin.register(BlogCategory)
class BlogCategoryAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):
    list_display = ['name']

    def get_image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' height='100px' width='100px' />".format(obj.image.url))

    get_image.short_description = 'Նկար'
    list_display.append('get_image')

