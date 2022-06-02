from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

from core.utils import CustomMetaModel, CustomLogoField, slug_generator


class BlogCategory(CustomMetaModel):
    name = models.CharField(max_length=255, verbose_name="Բաժնի անուն")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Հղում")
    breadcrumb_image = CustomLogoField(verbose_name='Բաժնի բանների նկար',
                                       blank=True, null=True, upload_to='blog-cat-bg-image/')
    breadcrumb_text = RichTextUploadingField(verbose_name="Բանների տեքստ", blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, verbose_name="Դասավորել")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-my_order']
        verbose_name = "Բլոգի բաժին"
        verbose_name_plural = "Բլոգի բաժիններ"

    def get_absolute_url(self):
        return reverse('blog_category', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.name, self.__class__)

        return super().save(*args, **kwargs)


class Blog(CustomMetaModel):
    category = models.ForeignKey(BlogCategory,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name="Ընտրել բաժինը")
    name = models.CharField(max_length=255, verbose_name="Վերնագիր")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name="Հղում")
    short_text = RichTextUploadingField(verbose_name="Հակիրճ տեքստ", blank=True, null=True)
    large_text = RichTextUploadingField(verbose_name="Ամբողջական տեքստ")
    views_count = models.PositiveIntegerField(default=0, editable=False)
    image = CustomLogoField(verbose_name='Գլխավոր նկար', blank=True, null=True, upload_to='blog-image/')
    my_order = models.PositiveIntegerField(default=0, verbose_name="Դասավորել")

    class Meta:
        ordering = ['-my_order']
        verbose_name = "Բլոգ"
        verbose_name_plural = 'Բլոգ'

    def get_absolute_url(self):
        return reverse('blog_details', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.name, self.__class__)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

