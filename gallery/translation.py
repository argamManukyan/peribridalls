from modeltranslation.translator import  TranslationOptions, register

from gallery.models import GalleryCategory


@register([GalleryCategory])
class StateTranslation(TranslationOptions):
    fields = ['name', 'breadcrumb_text', 'meta_title', 'meta_description']

