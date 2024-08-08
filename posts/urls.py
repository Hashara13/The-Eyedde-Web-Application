from django.urls import path
from . import views

#app_name='posts'

urlpatterns = [
    path('', views.post_home, name='post_home'),
    path('create/', views.post_create, name='post_create'),
    path('<slug:slug>/', views.post_content, name='post_content'),
]
