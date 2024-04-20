from django.urls import path
from . import views

app_name= "strona"

urlpatterns=[
    path('', views.main, name='main'),
    path('author/', views.author, name='author'),



]
