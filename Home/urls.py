from django.urls import path

from . import views

urlpatterns = [
    path('' ,views.hom),
    # path('two/',views.login),
    path('zero/',views.registration1),
    path('four/',views.about),
    path('five/',views.contact),
    path('six/',views.base),
    path('seven/',views.service),
    path('eight/',views.home1,name='eight'),
    path('nine/',views.home2,name='nine'),
    path('ten/',views.driverregistration),
    path('eleven',views.Views_bin,name='eleven'),
    path('twelve',views.Complaint,name='twelve'),
    path('feedback',views.feedback,name='feedback'),
    path('searchbar',views.searchbar,name='searchbar'),
    path('shopping',views.products,name='shopping'),
    path('news/', views.get_news, name='get_news'),
    path('cart/', views.cart, name='cart'),
    path('addcart/<id>/', views.addcart, name='addcart'),



]