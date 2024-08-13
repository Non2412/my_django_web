from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexPage, name= "index-page"),
    path("about/", views.aboutPage, name= "about-page"),
    path("contact/", views.contactPage, name= "contact-page"),
    path('for/', views.forPage, name="for-page"),
    path('card/', views.cardPage, name="card-page"),
    path('color/', views.cardColorPage, name="color-page"),

]
