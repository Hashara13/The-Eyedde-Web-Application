from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('posts/', include('posts.urls')), 
    path('', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()