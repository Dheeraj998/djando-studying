
from django.urls import path
from . import views
urlpatterns = [

    path('', views.demo, name='demo'),
    #multiple
    path('about/',views.about,name='about'),
    path('profile',views.profile,name='profile')
]
