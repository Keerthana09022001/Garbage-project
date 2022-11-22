from django.urls import path

from . import views

urlpatterns = [
    path('one/' ,views.hom),
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
    path('thirteen',views.searchbar,name='thirteen'),
    path('fourteen',views.searchresult,name='fourteen')

]