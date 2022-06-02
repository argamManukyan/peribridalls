from datetime import datetime

from .models import FooTerCategory, CompanyInformation, SocialShareButtons


def footer_categories(request):
    """ Return all footer categories for iterate and show items of categories,
        and return the current year and site domain
    """

    year = datetime.now().year

    return {
        "footer_categories": FooTerCategory.objects.all(),
        "year": year,
        # "domain": request.get_host(),
        "site": f"{request.scheme}://{request.get_host()}",
        # "captcha_public": CAPTCHA_PUBLIC_KEY
    }


def company_information(request):
    """ Return company information """

    return {"company_information": CompanyInformation.objects.all()}


def footer_follow_icons(request):
    """ Return all following icons for the website """

    return {'footer_follow_icons': SocialShareButtons.objects.all()}