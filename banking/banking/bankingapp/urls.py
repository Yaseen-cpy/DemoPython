from django.urls import path
from . import views
urlpatterns= [

    path('',views.index,name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('forms', views.forms, name='forms'),
    path('new', views.new, name='new'),

]