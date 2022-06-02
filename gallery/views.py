from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from breadcrumbs.models import BreadcrumbTexts
from gallery.models import GalleryCategory, Gallery


def gallery_list(request):

    gallery_list = Gallery.objects.all()
    gallery_categories = GalleryCategory.objects.all()
    st_content = BreadcrumbTexts.objects.filter(location='gallery').first()

    paginator = Paginator(gallery_list, 12)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj,
        'gallery_categories': gallery_categories,
        'st_content': st_content
    }

    return render(request, 'gallery.html', context)


def gallery_details(request, slug):
    gallery_category = get_object_or_404(GalleryCategory, slug=slug)
    images = Gallery.objects.filter(category=gallery_category)
    gallery_categories = GalleryCategory.objects.all()

    paginator = Paginator(images, 12)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        "gallery_category": gallery_category,
        "page_obj": page_obj,
        "gallery_categories": gallery_categories,
    }

    return render(request, 'gallery_category.html', context)
