from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('posts/', include('posts.urls')), 
    path('accounts/', include('users.urls')), 
    path('', views.home, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)