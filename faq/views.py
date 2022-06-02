from django.shortcuts import render

from breadcrumbs.models import BreadcrumbTexts
from faq.models import FAQ


def faq(request):
    faq_list = FAQ.objects.all()
    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='faq').first()
    context = {"faq_list": faq_list, 'st_content': st_content}
    return render(request, 'faq.html', context)
