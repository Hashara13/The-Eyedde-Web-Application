from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
]
