from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin

from faq.models import FAQ


@admin.register(FAQ)
class FAQAdmin(TabbedDjangoJqueryTranslationAdmin):
    pass