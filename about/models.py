from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
from core.utils import CustomModel, CustomLogoField


# class OurGoals(CustomModel):
#     my_order = models.PositiveIntegerField(verbose_name="Դասավորել", default=0)
#     name = models.CharField(max_length=255, verbose_name="Նպատակի անուն")
#     text = models.TextField(verbose_name="Նկարագրություն", blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         ordering = ['-my_order']
#         verbose_name = "Նպատակ"
#         verbose_name_plural = "Մեր նպատակները"


class OurAdvantages(CustomModel):
    icon = CustomLogoField(blank=True)
    name = models.CharField(max_length=255, verbose_name="Նպատակի անուն")
    text = models.TextField(verbose_name="Նկարագրություն", blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, verbose_name='Դասավորել')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Առավելություն"
        verbose_name_plural = "Մեր առավելությունները"
        ordering = ['my_order']


class AboutUs(CustomModel):

    text1 = RichTextUploadingField(verbose_name="«Մեր մասին» առաջին հատված")
    text2 = RichTextUploadingField(verbose_name="«Մեր մասին» երկրորդ հատված", blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Մեր մասին'


class AboutUsHomepage(CustomModel):
    text = RichTextUploadingField(verbose_name="Տեքստ")
    image = CustomLogoField(blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Մեր մասին -ի գլխավոր էջի կոնտենտ"


class AboutUsBanner(CustomModel):
    image = CustomLogoField()
    text = RichTextUploadingField(verbose_name="Տեքստ", blank=True, null=True)
    # url = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = "«Մեր մասին» բաններ"

