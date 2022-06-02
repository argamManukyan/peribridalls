# from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from modeltranslation.admin import TranslationInlineModelAdmin, TabbedDjangoJqueryTranslationAdmin
from singlemodeladmin import SingleModelAdmin

from contactus.models import ContactUsPage, FollowUsContactUs, ContactUsJoinUsData, Bookings, WorkingHours


class TabulaInlineContactJoinUs(TranslationInlineModelAdmin, admin.StackedInline):
    model = ContactUsJoinUsData
    extra = 0


class TabulaInlineContactFollow(TranslationInlineModelAdmin, admin.StackedInline):
    model = FollowUsContactUs
    extra = 0


@admin.register(ContactUsPage)
class ContactUsPageModelAdmin(SingleModelAdmin, TabbedDjangoJqueryTranslationAdmin):
    inlines = [TabulaInlineContactJoinUs, TabulaInlineContactFollow]


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date_of_book', 'time_of_pick']



admin.site.register(WorkingHours)