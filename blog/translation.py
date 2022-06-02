from modeltranslation.translator import TranslationOptions, register
from blog.models import BlogCategory, Blog


@register([BlogCategory])
class StateTranslation(TranslationOptions):
    fields = ['name', 'breadcrumb_text', 'meta_title', 'meta_description']


@register(Blog)
class StateTranslation(TranslationOptions):
    fields = ['name', 'large_text', 'short_text', 'meta_title', 'meta_description']

