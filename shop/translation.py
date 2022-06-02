from modeltranslation.translator import register, TranslationOptions
from shop.models import Category, FilterField, FilterValue, Color, Product, Brand


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = [
#         'name',
#         # 'homepage_name',
#         'short_description',
#         'large_description',
#         # 'notification_text',
#         'meta_title',
#         'meta_description'
#     ]


# @register(FilterField)
# class FilterFieldTranslationOptions(TranslationOptions):
#     fields = ['title',]


@register([FilterValue, FilterField])
class FilterValueTranslationOptions(TranslationOptions):
    fields = ['title']


@register([Brand, Category])
class FilterValueTranslationOptions(TranslationOptions):
    fields = ['meta_title', 'meta_description', 'name', 'breadcrumb_text']


@register(Color)
class ColorTranslationOptions(TranslationOptions):
    fields = ['title']


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ['name', 'short_text', 'large_text', 'meta_title', 'meta_description']
