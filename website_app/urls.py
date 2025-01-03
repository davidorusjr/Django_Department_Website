from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('contact.html', views.contact, name="contact"),
    path('abt_us_overview.html', views.overview, name="overview"),
    path('abt_us_philosophy.html', views.philosophy, name="philosophy"),
    path('abt_us_admission.html', views.admission, name="admission"),
]
