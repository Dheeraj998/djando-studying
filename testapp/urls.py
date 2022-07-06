
from django.urls import path
from . import views
urlpatterns = [

    path('', views.demo, name='demo'),
    #multiple
    path('add/',views.addition,name='addition'),
    path('profile',views.profile,name='profile'),
    #  path('add/',views.addition,name='addition'),
]
