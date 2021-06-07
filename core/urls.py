from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.frontpage, name="home"),
    path('contact-us/', views.contactpage, name="contact"),
]
