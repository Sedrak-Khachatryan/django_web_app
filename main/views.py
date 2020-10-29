from django.shortcuts import render
from .models import ContactForm, News
from django.http import HttpResponse
from .forms import ContactFormBack
from django.core.mail import send_mail
from django.conf import settings


def index(request):     # Home page view
    news = News.objects.order_by('-date')
    return render(request, 'main/index.html',
                  {'title': 'dors craft beer & kitchen ',
                   'news': news})


def about(request):     # About us view
    data = {
        'title': 'About us'
    }
    return render(request, 'main/about.html', data)


def kitchen(request):   # Kitchen view
    data = {
        'title': 'Kitchen'
    }
    return render(request, 'main/kitchen.html', data)


def craft_beer(request):    # Craft beer view
    data = {
        'title': 'Craft Beer'
    }
    return render(request, 'main/craft_beer.html', data)


def contact_us(request):     # Contact form and email sending
    if request.method == 'POST':
        form = ContactFormBack(request.POST)
        if form.is_valid():
            # send email code goes here

            message = "{0} has sent you a new message:\n{1}".format(form.cleaned_data['phone'],
                                                                    form.cleaned_data['message'],
                                                                    )
            send_mail(form.cleaned_data['email'],
                      message,
                      settings.EMAIL_HOST_USER,
                      ['sedrak.g.khachatryan@gmail.com'],
                      fail_silently=False,)
            # to db
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            message = request.POST.get('message', "")
            phone_number = request.POST.get('phone', "")
            new_contact = ContactForm(name=name, email=email, message=message, phone_number=phone_number)
            new_contact.save()
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactFormBack()

    return render(request, 'main/contact_us.html', {'form': form})


# craft beer views

def farmhouse_ale(request):
    data = {
        'title': 'Farmhouse Ale'
    }
    return render(request, 'main/farmhouse_ale.html', data)


def bavarian_weizen(request):
    data = {
        'title': 'Bavarian Weizen'
    }
    return render(request, 'main/bavarian_weizen.html', data)


def dark_lager(request):
    data = {
        'title': 'Dark Lager'
    }
    return render(request, 'main/dark_lager.html', data)


def apa(request):
    data = {
        'title': 'A.P.A.'
    }
    return render(request, 'main/apa.html', data)


def ipa(request):
    data = {
        'title': 'I.P.A.'
    }
    return render(request, 'main/ipa.html', data)


def dipa(request):
    data = {
        'title': 'D.I.P.A.'
    }
    return render(request, 'main/dipa.html', data)


def apple_cider(request):
    data = {
        'title': 'Apple Cider'
    }
    return render(request, 'main/apple_cider.html', data)


def cherry_ale(request):
    data = {
        'title': 'Cherry Ale'
    }
    return render(request, 'main/cherry_ale.html', data)

# Menu views
