from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin, TranslationTabularInline
from easy_select2 import select2_modelform

from .models import *

# footerForm = select2_modelform(FooterItems)


@admin.register(CompanyInformation)
class CompanyInformationAdmin(TabbedDjangoJqueryTranslationAdmin):
    list_display = ['id', 'text']

    def get_icon(self, obj):
        if obj.icon:
            return mark_safe("<img src='{}' height='30px' width='30px' />".format(obj.icon.url))
        return ''

    get_icon.short_description = "Նկար"
    list_display += ['get_icon']


@admin.register(FooTerCategory)
class FooTerCategoryAdmin(TabbedDjangoJqueryTranslationAdmin):
    pass


@admin.register(FooterItems)
class FooterItemsAdmin(TabbedDjangoJqueryTranslationAdmin):
    # form = footerForm
    pass

@admin.register(SocialShareButtons)
class SocialShareButtonsAdmin(admin.ModelAdmin):
    pass

