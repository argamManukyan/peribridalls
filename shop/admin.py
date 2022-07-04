from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_select2 import select2_modelform
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin
from mptt.admin import DraggableMPTTAdmin

from shop.models import Product, ProductImage, ProductFeature, Category, FilterValue, FilterField, Brand, Color

ProductForm = select2_modelform(Product,  attrs={"width": "250px"})
FilterFieldForm = select2_modelform(FilterField)


class ProductImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductFeatureInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductFeature
    extra = 0
    form = select2_modelform(model,  attrs={"width": "250px"})


@admin.register(Category)
class CategoryAdmin(TabbedDjangoJqueryTranslationAdmin, DraggableMPTTAdmin):
    exclude = ['large_description']
    form = select2_modelform(Category, attrs={"width": "250px"})

    # def get_fields(self, request, obj=None):
    #     resp = super().get_fields(request, obj)
    #     if 'meta_title' in resp:
    #         return set_meta_fields_before_form(resp)
    #     return resp


class ProductAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):
    inlines = [ProductFeatureInlineAdmin, ProductImageInlineAdmin]
    form = ProductForm
    list_filter = ['category']
    search_fields = ['name', 'name_ru', 'name_en']

    def get_image(self, obj):
        if obj.main_image:
            return mark_safe('<img src="{}" height="200px" width="200px" />'.format(obj.main_image.url))

    get_image.short_description = "Նկար"
    list_display = ['name','get_image']


admin.site.register(Product, ProductAdmin)


@admin.register(Color)
class ColorAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):
    def get_color(self, obj):
        if obj.color_code:
            return mark_safe(f'<div style=" width: 400px;height: 40px; background: {obj.color_code};"></div>')

    get_color.short_description = "Երանգը"

    list_display = ['id', 'title', 'get_color']


@admin.register(FilterField)
class FilterFieldModelAdmin(TabbedDjangoJqueryTranslationAdmin):
    form = FilterFieldForm


@admin.register(FilterValue)
class FilterValueModelAdmin(TabbedDjangoJqueryTranslationAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):

    def get_logo(self, obj: Brand):
        if obj.icon:
            return mark_safe('<img src="{}" height="50px" width="50px" />'.format(obj.icon.url))
        return ''

    get_logo.short_description = "Լոգո"

    def get_image(self, obj: Brand):
        if obj.image:
            return mark_safe('<img src="{}" height="50px" width="50px" />'.format(obj.image.url))
        return ''

    get_image.short_description = "Նկար"

    list_display = ['id', 'name', 'get_logo', 'get_image']
