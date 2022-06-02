from django.http import Http404
from django.template import Library
from core.middleware import current_request
from shop.models import Category, Brand

register = Library()


@register.simple_tag
def my_url(value, field, urlencode=None):
    url = '?{}={}'.format(field, value)

    if urlencode:
        querystring = urlencode.split('&')

        filtered_queryset = filter(lambda p: p.split('=')[0] != field, querystring)
        encode_qs = '&'.join(filtered_queryset)
        if encode_qs:
            url += '&{}'.format(encode_qs)
    return url

@register.filter(name='unique')
def unique(qs):
    req = current_request()

    try:
        cat_slug = req.resolver_match.kwargs.get('slug')
        if req.resolver_match.url_name in ['brand_list', 'brand_details']:
            category = Brand.objects.get(slug__iexact=cat_slug)
        else:
            category = Category.objects.get(slug__iexact=cat_slug)
        if isinstance(category, Category):
            if category.is_leaf_node():
                list_ids = [category.id]
            else:
                list_ids = [i.id for i in category.get_descendants(include_self=True)]
        else:
            list_ids = [category.id]

    except Exception as e:
        pass

    qs_array = []
    num_array = []
    if isinstance(category, Category):
        qs = qs.filter(product__category__in=list_ids)
    else:
        qs = qs.filter(product__brand__in=list_ids)

    for i in qs:
        if i.value not in qs_array:
            qs_array.append(i.value)

    if num_array:
        num_array = sorted(num_array, key=lambda x: int(x.split(" ")[0]))
    qs_array.extend(num_array)
    return qs_array
