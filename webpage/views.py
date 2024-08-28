from django.shortcuts import render, HttpResponse


def indexPage(request):
    return render(request, 'index.html')


def aboutPage(request):
    return render(request, 'about.html')


def contactPage(request):
    return render(request, 'contact.html')


def simpleFormPage(request):
    return render(request, 'form_page.html')


def forPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'for_test.html', context)


def cardPage(request):
    context = {}
    lt = list(range(0, 100))
    context["list"] = lt

    return render(request, 'card.html', context)


def cardColorPage(request):
    context = {
        'color': '',
    }

    if request.method == "GET":
        context['color'] = request.GET.get('color', '')

    return render(request, 'card_color.html', context)


def formPage(request):
    email = ''
    password = ''

    context = {}

    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('my-password', '')

    context['email'] = email
    context['password'] = password

    return render(request, 'form_page.html', context)