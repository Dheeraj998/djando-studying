
from django.urls import path
from . import views
urlpatterns = [

    path('', views.demo, name='demo'),
    #multiple
    path('add/',views.addition,name='addition'),
    path('profile',views.profile,name='profile'),
    path('login/',views.login,name='login'),
    path('renderHtmlPage/',views.renderhtmlPage,name='renderhtmlPage'),
    path('loginhtml/',views.loginHtml,name='loginHtml'),


    # path('ll/',views.ll,name='ll')
    #  path('add/',views.addition,name='addition'),
]
