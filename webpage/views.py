from django.shortcuts import render, HttpResponse

def indexPage(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html')

def contactPage(request):
    return render(request, 'contact.html')

def forPage(request):
    return render(request, 'for_test.html')

def forPage(request):
    context = {}
    lt = list(range(0,100))
    context["list"] = lt

    return render(request, 'for_test.html', context)   