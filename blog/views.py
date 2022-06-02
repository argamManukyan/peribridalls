from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import BlogCategory, Blog
from breadcrumbs.models import BreadcrumbTexts


def blog_category(request, slug):
    category = get_object_or_404(BlogCategory, slug=slug)
    posts = Blog.objects.filter(category=category)
    categories = sorted(BlogCategory.objects.all(), key=lambda x: x.id == category.id, reverse=True)

    paginator = Paginator(posts, settings.PAGE_SIZE_FOR_BLOG)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    print(len(page_obj.object_list))
    context = {
        "category": category,
        "categories": categories,
        "page_obj": page_obj
    }
    return render(request, 'blog_category.html', context)


def blog_list(request):
    posts = Blog.objects.all()
    categories = BlogCategory.objects.all()
    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='blog').first()

    paginator = Paginator(posts, settings.PAGE_SIZE_FOR_BLOG)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        "categories": categories,
        "page_obj": page_obj,
        "st_content": st_content
    }
    return render(request, 'blog.html', context)


def blog_details(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    related_posts = Blog.objects.exclude(id=post.id).order_by('?')[:2]

    if post.slug not in request.session:
        request.session[post.slug] = post.slug
        post.views_count += 1
        post.save()

    context = {
        "related_posts": related_posts,
        "post": post,
    }
    return render(request, 'blog_full.html', context)

