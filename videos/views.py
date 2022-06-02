from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from breadcrumbs.models import BreadcrumbTexts
from .models import Video


class VideoList(ListView):
    template_name = 'peri_tv.html'
    paginate_by = 12
    model = Video.objects.all()


def video_list(request):

    videos = Video.objects.all()

    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='peri_tv').first()

    page = request.GET.get('page', 1)
    paginator = Paginator(videos, 8)
    page_obj: Video = paginator.get_page(page)

    context = {'page_obj': page_obj, 'st_content': st_content}
    return render(request, 'peri_tv.html', context)



