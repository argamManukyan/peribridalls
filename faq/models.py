from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import safe


class FAQ(models.Model):
    question = RichTextUploadingField(max_length=500, verbose_name='Հարց')
    answer = RichTextUploadingField(verbose_name='Պատասխան')

    def __str__(self):
        return safe(self.question)

    class Meta:
        verbose_name = 'Հաճախակի տրվող հարց'
        verbose_name_plural = 'Հաճախակի տրվող հարցեր'
