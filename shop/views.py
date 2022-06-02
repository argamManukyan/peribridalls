from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.decorators.cache import never_cache
from about.models import AboutUsHomepage, AboutUsBanner
from blog.models import Blog
from breadcrumbs.models import BreadcrumbTexts
from contactus.email import SendMailThread
from contactus.forms import BookingsForm
from contactus.models import ContactUsJoinUsData, WorkingHours, Bookings
from header.models import Slider
from .models import *


def paginated_response(request, items, limit=12):
    page = request.GET.get('page', 1)
    paginator = Paginator(items, limit)
    page_obj = paginator.get_page(page)
    return page_obj


def brand_list(request):
    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='brands').first()
    brands = Brand.objects.all()

    context = {"st_content": st_content, "brands": brands}

    return render(request, 'all_brands.html', context)


def products_list(request):
    products = Product.objects.all()
    products_sort = sorted(products)

    page_obj = paginated_response(request, products)
    colors = Color.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    filter_fields = FilterField.objects.filter(Q(show_in_filters=True),
                                               Q(productfeature__value__isnull=False)).distinct()

    featured_values = FilterValue.objects.filter(Q(productfeature__field__show_in_filters=True),
                                                 Q(productfeature__value__isnull=False)).distinct()
    st_content = BreadcrumbTexts.objects.filter(location='products')
    context = {
        'page_obj': page_obj,
        'colors': colors,
        'brands': brands,
        'filter_fields': filter_fields,
        'featured_values': featured_values,
        'st_content': st_content,
        'categories': categories,
    }

    return render(request, 'product_list.html', context)


def category_list(request):
    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='categories').first()
    categories = Category.objects.filter(parent=None)
    context = {'categories': categories, 'st_content': st_content}
    return render(request, 'all_categories.html', context)


@never_cache
def brand_details(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    categories = Category.objects.filter(parent=None)

    filter_fields = FilterField.objects.filter(Q(productfeature__product__brand__slug=slug, show_in_filters=True),
                                               Q(productfeature__value__isnull=False)).distinct()

    featured_values = FilterValue.objects.filter(Q(productfeature__product__brand__slug=slug,
                                                   productfeature__field__show_in_filters=True),
                                                 Q(productfeature__value__isnull=False)).distinct()

    colors = Color.objects.filter().distinct()
    brands = Brand.objects.all()
    products = Product.objects.filter(brand=brand)
    page_obj = paginated_response(request, products)

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return show_filter_data(request, products)

    context = {
        'brand': brand,
        'filter_fields': filter_fields,
        'featured_values': featured_values,
        'colors': colors,
        'categories': categories,
        'brands': brands,
        'page_obj': page_obj,
    }

    return render(request, 'brand_details.html', context)


def filter_products(request, products) -> list:
    url_kwargs = {}

    for item in request.GET:
        if len(request.GET.getlist(item)) > 1:
            url_kwargs[item] = request.GET.getlist(item)
        else:
            url_kwargs[item] = request.GET.get(item)
    q_condition_queries = []

    for key, value in url_kwargs.items():
        if key not in ['min_price', 'max_price', 'page', 'sorting', 'top_filter', 'type', 'q', 'brands']:
            if isinstance(value, list):
                if key == 'color':
                    for i in value:
                        if not i.isdigit():
                            value.remove(i)

                    q_condition_queries.append(
                        {'color_id__in': value})
                else:
                    q_condition_queries.append(
                        {f'productfeature__field__filter_key': key, 'productfeature__value__title__in': value})
            else:
                if key == 'color':
                    if value.isdigit():
                        q_condition_queries.append({'color_id': value})
                else:
                    q_condition_queries.append(
                        {f'productfeature__value__title': value, 'productfeature__field__filter_key': key})

    if request.GET.get('min_price'):
        products = products.filter(finally_price__gte=int(request.GET.get('min_price')))
    if request.GET.get('max_price'):
        products = products.filter(finally_price__lte=int(request.GET.get('max_price')))

    if request.GET.get('brands'):
        products = products.filter(brand_id__in=request.GET.getlist('brands'))

    if len(q_condition_queries):
        for filter_item in q_condition_queries:
            products = products.filter(**filter_item).distinct()
    if request.GET.get('sorting'):
        products = products.order_by(request.GET.get('sorting'))
    else:
        products = products.order_by('-id')
    return paginated_response(request, products)


def show_filter_data(request, products):
    data = {
        "link": request.GET.urlencode(),
        "products": render_to_string('includes/filtered_items.html', context={
            "page_obj": filter_products(request, products),
        }, request=request)
    }

    return JsonResponse(data)


@never_cache
def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)

    filter_fields = FilterField.objects.filter(Q(productfeature__product__category__slug=slug,
                                                 show_in_filters=True),
                                               Q(productfeature__value__isnull=False)).distinct()

    featured_values = FilterValue.objects.filter(Q(productfeature__product__category__slug=slug,
                                                   productfeature__field__show_in_filters=True),
                                                 Q(productfeature__value__isnull=False)).distinct()

    colors = Color.objects.filter().distinct()
    brands = Brand.objects.all()
    products = Product.objects.filter(category__in=category.get_family().values_list('id', flat=True))
    page_obj = filter_products(request, products)
    categories = Category.objects.filter(parent=None)

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return show_filter_data(request, products)

    context = {
        'category': category,
        'categories': categories,
        'filter_fields': filter_fields,
        'colors': colors,
        'brands': brands,
        'page_obj': page_obj,
        'featured_values': featured_values,
    }

    return render(request, 'category.html', context)


def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    others = Product.objects.filter(Q(brand=product.brand)
                                    | Q(category=product.category),
                                    ~Q(id=product.id)).distinct()

    contact_details = ContactUsJoinUsData.objects.all()

    context = {
        'product': product,
        'others': others,
        'contact_details': contact_details,
    }

    return render(request, 'product_page.html', context)


def home_page(request):
    about_home: AboutUsHomepage = AboutUsHomepage.objects.last()
    brands = Brand.objects.all()
    posts = Blog.objects.order_by('-id')[:2]
    banner: AboutUsBanner = AboutUsBanner.objects.last()
    categories: Category = Category.objects.filter(parent=None)
    slider = Slider.objects.all()
    working_hours = WorkingHours.objects.all()
    form = BookingsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            f = form.save()
            time_of_pick = None
            if request.POST.get('time_of_pick', None):
                if request.POST.get('time_of_pick', None) != 'select':
                    time_of_pick = WorkingHours.objects.filter(id=request.POST.get('time_of_pick')).first()
                    Bookings.objects.filter(id=f.id).update(time_of_pick_id=request.POST.get('time_of_pick'))
            data = {
                'action': 'booking',
                'request': request,
                'name': form.name,
                'phone': form.phone,
                'date_of_book': form.date_of_book,
                'time_of_pick': time_of_pick

            }
            SendMailThread(data).start()
            messages.success(request, 'Your request has been successfully sent.<br>Our manager will contact you soon.')
        else:

            messages.error(request, 'Something went wrong, please try again')
        return redirect(reverse('shop:home_page') + '#appointment')

    context = {
        'about_home': about_home,
        'brands': brands,
        'posts': posts,
        'banner': banner,
        'slider': slider,
        'working_hours': working_hours,
        'categories': categories,
    }

    return render(request, 'index.html', context)


#
# class SearchView(View):
#
#     def get(self, request, **kwargs):
#         q = request.GET.get('q', '')
#
#         qs = Blog.objects.all()
#         qs1 = Brand.objects.all()
#         qs2 = Product.objects.all()
#         if q:
#             qs = qs.filter(Q(name__icontains=q) | Q(slug__icontains=q)).distinct()
#             qs1 = qs1.filter(Q(name__icontains=q) | Q(slug__icontains=q)).distinct()
#             qs2 = qs2.filter(Q(name__icontains=q) | Q(slug__icontains=q)).distinct()
#
#         queryset = (qs, qs1, qs2)
#         results = []
#
#         for i in queryset:
#             for j in i:
#                 results.append(j)
#
#         context = {'q': q}
#
#         return render(request, 'search.html', context)

def search(request):
    q = request.GET.get('q', None)
    qs = Blog.objects.all()
    qs1 = Brand.objects.all()
    qs2 = Product.objects.all()
    n = q
    if q not in ['', ' '] and q is not None:
        q = q.replace(' ', '-')
        qs = qs.filter(Q(name__icontains=q) | Q(slug__icontains=q)).distinct()
        qs1 = qs1.filter(Q(name__icontains=q) | Q(slug__icontains=q)).distinct()
        qs2 = qs2.filter(Q(name__icontains=q) | Q(slug__icontains=q)).distinct()

    queryset = []
    queryset.extend([i for i in qs])
    queryset.extend([i for i in qs1])
    queryset.extend([i for i in qs2])

    q = n if n is not None and n not in [" ", ""] else ''
    context = {
        'q': q,
        'results': queryset
    }

    return render(request, 'search.html', context)
