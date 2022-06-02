from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Video

@admin.register(Video)
class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

