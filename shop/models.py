from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse
from mptt.models import TreeForeignKey, MPTTModel
from unidecode import unidecode

from core.utils import CustomLogoField, CustomMetaModel, slug_generator, smart_strip, CustomModel


class Brand(CustomMetaModel):
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Անուն")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="Հղում")
    image = CustomLogoField(blank=True, null=True)
    icon = CustomLogoField(verbose_name="Լոգո", blank=True, null=True)
    breadcrumb_image = CustomLogoField(verbose_name="Breadcrumb -ի նկար", blank=True, null=True)
    breadcrumb_text = models.TextField(blank=True, verbose_name="Breadcrumb -ի տեքստ")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Բրենդ'
        verbose_name_plural = 'Բրենդներ'

    def get_absolute_url(self):
        return reverse('shop:brand_details', kwargs={"slug": self.slug})


class Category(MPTTModel):
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(max_length=300, blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Անուն")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="Հղում")
    image = CustomLogoField(blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                            related_name='children', verbose_name="Հայրական բաժին")
    breadcrumb_image = CustomLogoField(verbose_name="Breadcrumb -ի նկար", blank=True, null=True)
    breadcrumb_text = models.TextField(blank=True, verbose_name="Breadcrumb -ի տեքստ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        title_list = [self.name]
        parent = self.parent

        while parent is not None:
            title_list.append(parent.name)
            parent = parent.parent

        return '-->'.join(title_list[::-1]) or ''

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.name)
        super().save(*args, **kwargs)

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Բաժին'
        verbose_name_plural = 'Բաժիններ'

    def get_absolute_url(self):
        return reverse('shop:category_details', kwargs={"slug": self.slug})


class FilterField(models.Model):
    """ Filter field table """
    FIELD_TYPES = [
        ('radio', 'Radio'),
        ('select', 'Dropdown'),
    ]

    category = models.ManyToManyField(Brand, verbose_name='Բրենդ', )
    filter_key = models.CharField(max_length=150, unique=True, blank=True, editable=False)
    title = models.CharField(verbose_name='Դաշտի անուն', max_length=255, unique=True)
    show_in_filters = models.BooleanField(verbose_name='Ցուցադրել ֆիլտրերում', default=False)
    # is_main = models.BooleanField(verbose_name='Հիմնական դաշտ', default=False)
    # field_type = models.TextField(choices=FIELD_TYPES, blank=True, null=True, max_length=50, verbose_name='Դաշտի տիպը')
    # help_field_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Օգնող դաշտի վերնագիր')
    # help_field_content = RichTextUploadingField(blank=True, null=True, verbose_name='Օգնող դաշտի տեքստ')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.filter_key:
            self.filter_key = unidecode(self.title.replace(' ', '_'))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ֆիլտրացման դաշտ'
        verbose_name_plural = 'Ֆիլտրացման դաշտեր'


class FilterValue(models.Model):
    """ Filter value table """

    title = models.CharField(verbose_name='Ֆիլտրացման արժեք', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ֆիլտրվող արժեքներ'
        verbose_name_plural = 'Ֆիլտրվեղ արժեքներ'

    def save(self, *args, **kwargs):
        self.title = smart_strip(self.title)
        super().save(*args, **kwargs)


class Product(CustomMetaModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Բաժին")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Բրենդ")
    name = models.CharField(max_length=255, verbose_name="Անուն")
    slug = models.SlugField(blank=True, null=True, unique=True, verbose_name="Հղում")
    main_image = CustomLogoField()
    short_text = RichTextUploadingField(blank=True, null=True, verbose_name="Հակիրճ տեքստ")
    large_text = RichTextUploadingField(blank=True, null=True, verbose_name="Ամբողջական տեքստ")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Դասավորել')
    color = models.ForeignKey('Color', on_delete=models.SET_NULL,
                              null=True, blank=True, verbose_name="Գույն")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generator(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['my_order']
        verbose_name = "Ապրանք"
        verbose_name_plural = "Ապրանքներ"

    def get_absolute_url(self):
        return reverse('shop:product_details', kwargs={"slug": self.slug})


class Color(CustomModel):
    """ Color table """
    title = models.CharField(verbose_name='Գույնի անուն', max_length=255)
    color_code = ColorField(default="#fff", blank=True, null=True, verbose_name='Գույնի կոդ')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Դասավորել')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['my_order']
        verbose_name = 'Գույն'
        verbose_name_plural = 'Գույներ'


class ProductImage(CustomModel):
    """ Product images table """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = CustomLogoField(upload_to='product-img/')
    my_order = models.PositiveIntegerField(default=0, verbose_name='Դասավորել')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Ապրանքի նկար'
        verbose_name_plural = 'Ապրանքի նկարներ'
        ordering = ['my_order']


class ProductFeature(CustomModel):
    """ Product feature table """

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                verbose_name='Ապրանքի անուն',
                                )
    field = models.ForeignKey(FilterField, verbose_name='Դաշտ', on_delete=models.SET_NULL, null=True)
    value = models.ForeignKey(FilterValue, verbose_name='Դաշտի արժեք', on_delete=models.SET_NULL, null=True)
    # measure_unit = models.ForeignKey(
    #     'UnitMeasurement',
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     verbose_name='Չափման միավոր'
    # )
    # price = models.IntegerField(verbose_name='Գին', default=0)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Դասավորել')
    is_active = models.BooleanField(default=True, verbose_name='Ակտիվ է')
    # show_on_product_block = models.BooleanField(default=False, verbose_name='Ցուցադրել ապրանքի բլոկում')

    def __str__(self):
        return f'{self.product.name} - {self.value}'

    class Meta:
        verbose_name = 'Ապրանքի չափորոշիչ'
        verbose_name_plural = 'Ապրանքի չափորոշիչներ'
        unique_together = ['product', 'field', 'value']
        ordering = ['my_order']



