from django.shortcuts import render

from blog.models import Blog
from .models import *
from breadcrumbs.models import BreadcrumbTexts


def about_us(request):
    about: AboutUs = AboutUs.objects.first()
    advantages = OurAdvantages.objects.all()
    banner: AboutUsBanner = AboutUsBanner.objects.last()
    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='abouts').first()
    posts = Blog.objects.order_by('?')[:2]
    context = {
        'about': about,
        'advantages': advantages,
        'banner': banner,
        'st_content': st_content,
        'posts': posts,
    }

    return render(request, 'about_us.html', context)