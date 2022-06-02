from modeltranslation.translator import TranslationOptions, register

from faq.models import FAQ


@register(FAQ)
class FAQTrans(TranslationOptions):
    fields = ['question', 'answer']
