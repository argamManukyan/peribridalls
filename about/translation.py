from modeltranslation.translator import TranslationOptions, register

from .models import AboutUs, AboutUsHomepage, AboutUsBanner, OurAdvantages


@register(AboutUs)
class AboutUsPageTrans(TranslationOptions):
    fields = ['text1', 'text2']


@register(AboutUsHomepage)
class AboutUsHomepageTrans(TranslationOptions):
    fields = ['text']


@register(AboutUsBanner)
class AboutUsHomepageTrans(TranslationOptions):
    fields = ['text', 'url']


@register(OurAdvantages)
class OurAdvantagesTrans(TranslationOptions):
    fields = ['name', 'text']
