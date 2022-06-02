from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from core.utils import CustomMetaModel, CustomModel, CustomLogoField, slug_generator


class GalleryCategory(CustomMetaModel):
    name = models.CharField(max_length=255, verbose_name="Բաժնի անուն")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Հղում")
    my_order = models.PositiveIntegerField(default=0, verbose_name="Դասավորել")
    breadcrumbs_image = CustomLogoField(verbose_name='Բաժնի բանների նկար', blank=True, null=True,
                                        upload_to='gallery-category-bg/')
    breadcrumb_text = RichTextUploadingField(verbose_name="Բանների տեքստ", blank=True, null=True,)

    def get_absolute_url(self):
        return reverse('gallery_details', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-my_order']
        verbose_name = "Տեսադարանի բաժին"
        verbose_name_plural = "Տեսադարանի բաժիններ"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.name, self.__class__)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Gallery(CustomModel):
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL,
                                 null=True, blank=True, verbose_name="Ընտրել բաժինը")
    image = CustomLogoField(upload_to='gallery/')
    my_order = models.PositiveIntegerField(default=0, verbose_name="Դասավորել")

    class Meta:
        ordering = ['-my_order']
        verbose_name = "Նկար"
        verbose_name_plural = "Տեսադարան"

