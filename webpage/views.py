from django.shortcuts import render, HttpResponse

def indexPage(request):
    return HttpResponse("hello, world")

def aboutUs(request):
    return HttpResponse("รักอ.ว่านมากเลยครับ")

def contactUs(request):
    return HttpResponse("ติดต่อฉัน")

