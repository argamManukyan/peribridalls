from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
import requests
import json
from breadcrumbs.models import BreadcrumbTexts
from .email import SendMailThread
from .forms import ContactUsRequestForm
from .models import ContactUsPage


def contact_us(request):
    form = ContactUsRequestForm(request.POST or None)
    st_content: BreadcrumbTexts = BreadcrumbTexts.objects.filter(location='contacts').first()
    contactuspage: ContactUsPage = ContactUsPage.objects.first()
    captcha_public = settings.CAPTCHA_PUBLIC
    if request.method == 'POST':
        if form.is_valid():
            captcha_token = request.POST.get("g-recaptcha-response")
            cap_url = "https://www.google.com/recaptcha/api/siteverify"
            cap_secret = settings.CAPTCHA_SECRET
            cap_data = {"secret": cap_secret, "response": captcha_token}
            cap_server_response = requests.post(url=cap_url, data=cap_data)
            cap_json = json.loads(cap_server_response.text)

            if cap_json['success'] is False:
                if request.LANGUAGE_CODE == 'hy':
                    messages.error(request, 'Տեղի է ունեցել սխալ, փորձեք կրկին')
                elif request.LANGUAGE_CODE == 'ru':
                    messages.error(request, 'Что то пошло не так, попробуйте еще раз')
                elif request.LANGUAGE_CODE == 'en':
                    messages.error(request, 'Something went wrong, please try again')
                return redirect('contacts')

            form = form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your message has been successfully sent.<br>Our manager will contact you soon.')

            data = {
                'action': 'contact',
                'request': request,
                'first_name': form.first_name,
                'phone1': form.phone1,
                'email': form.email,
                'message': form.messages,
            }
            SendMailThread(data).start()
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong, please try again')
        return redirect('contact_us')

    return render(request, 'contacts.html', {'st_content': st_content, 'contactuspage': contactuspage,   'captcha_public': captcha_public,})
