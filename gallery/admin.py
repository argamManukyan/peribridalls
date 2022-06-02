from adminsortable2.admin import SortableAdminMixin
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin

from gallery.models import Gallery, GalleryCategory


class GalleryUploadForm(forms.ModelForm):
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Gallery
        fields = "__all__"


@admin.register(Gallery)
class GalleryImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = GalleryUploadForm

    def save_model(self, request, obj, form, change):
        obj.save()
        img_list = request.FILES.getlist('image')[:-1]
        for i in img_list:
            Gallery.objects.create(category_id=obj.category.id, image=i)

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:150px;height:150px;margin-right:10px" /> ')

    image_tag.short_description = 'Նկար'

    list_display = ['image_tag', 'category']


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(SortableAdminMixin, TabbedDjangoJqueryTranslationAdmin):
    pass

