from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('nforegistration',views.nforegistration,name='nforegistration'),
    path('page1',views.page1,name='page1'),
    path('nfologin',views.nfologin,name='nfologin'),
    path('nfoform1',views.nfoform1,name='nfoform1'),
    path('nfoform2',views.nfoform2,name='nfoform2'),
    path('nfoform3',views.nfoform3,name='nfoform3'),
    path('nfovoterdetails',views.nfovoterdetails,name='nfovoterdetails'),
    ]
