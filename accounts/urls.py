from django.urls import path
from . import views

from .import views
from django.contrib.auth import views as auth_views
# from django.conf import settings
# from django.conf.urls.static import static
#  from django.contrib.auth import views as auth_views
urlpatterns =[
    path('registration1',views.signup,name='registration1'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('index',views.index,name='index'),
    path('base',views.base,name='base'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('services', views.services, name='services'),
    path('home2', views.home2, name='home2'),
    path('change_password',views.change_password,name='change_password'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('payment_page',views.payment_page,name='payment_page'),
    path('payment_done/',views.payment_done,name='payment_done')


 ]

