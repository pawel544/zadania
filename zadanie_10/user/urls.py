from django.urls import path
from . import views

app_name='user'

urlpatterns=[
        path('signup/', views.signupuser, name='signup' ),
        path('login/',views.loginuser, name='login'),
        path('logaut/', views.logautuser, name='logaut')


]