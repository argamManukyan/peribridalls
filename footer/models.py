from django.db import models
from core.utils import CustomLogoField, CustomModel


class CompanyInformation(models.Model):
    icon = CustomLogoField(blank=True)
    text = models.CharField(max_length=255, verbose_name="Տեքստ")
    name = models.CharField(max_length=255, verbose_name='Դաշտի անուն')
    url = models.CharField(max_length=1000, verbose_name="Հղում", blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        # ordering = ['my_order']
        verbose_name = 'Կոնտակտային տվյալ'
        verbose_name_plural = 'Կոնտակտային տվյալներ'


class FooTerCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Անուն")

    def __str__(self):
        return self.name

    class Meta:
        # ordering = ['my_order']
        verbose_name = 'Footer -ի բաժին'
        verbose_name_plural = 'Footer -ի բաժիններ'


class FooterItems(CustomModel):
    category = models.ForeignKey(FooTerCategory,
                                 on_delete=models.RESTRICT,
                                 blank=True,
                                 verbose_name='Բաժին',
                                 null=True)
    name = models.CharField(max_length=255, unique=True, verbose_name="Անուն")
    url = models.URLField(verbose_name="Ամբողջական հղում")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Footer -ի հղումներ'
        verbose_name_plural = 'Footer -ի հղումներ'


class SocialShareButtons(CustomModel):
    icon = CustomLogoField()
    url = models.URLField(verbose_name='Ամբողջական հղում')
    name = models.CharField(max_length=255, unique=True, verbose_name="Անուն (alt)")

    def __str__(self):
        return self.name

    class Meta:
        # ordering = ['my_order']
        verbose_name = 'Սոց. ցանցի լոգո'
        verbose_name_plural = 'Սոց. ցանցերի լոգոներ'
