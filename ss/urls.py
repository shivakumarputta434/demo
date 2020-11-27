from django.urls import path
from .import views
from .import views2
from django.conf import settings
from django.conf.urls.static import static



#from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns=[
    path('home',views.home,name='home'),
    path('home1',views.home1,name='home1'),
    path('test',views.test,name='test'),
    path('download_csv',views.download_csv,name='download_csv'),
    path('wscrap',views.wscrap,name='wscrap'),
    path('wscrapJsonResponse',views.wscrapJsonResponse,name='wscrapJsonResponse'),
    path('weather',views.weather,name='weather'),
    path('display-movies-api/', views.MovieApi.as_view(), name='displaymoviesapi'),
    path('display-movies-api/<int:pk>/', views.MovieApi.as_view(), name='update'),
    path('hotel',views.hotel,name='hotel'),
    path('socialapp',views.socialapp,name='socialapp'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('insertgallery/<int:id>',views.insertgallery,name='insertgallery'),
    path('deleteimage/<int:id>',views.deleteimage,name='deleteimage'),
    path('updateimage/<int:id>',views.updateimage,name='updateimage'),
    path('testurls/<int:id>',views.testurls,name='testurls'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)