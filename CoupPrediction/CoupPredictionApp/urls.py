from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('datasets', views.datasets_page, name='datasets'),
    path('index', views.index, name='index')
]
