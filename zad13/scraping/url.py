from django.urls import path
from . import views

app_name= "scraping"

urlpatterns=[path('', views.scrap_and_fill_database, name="scrap_and_fill_database")]