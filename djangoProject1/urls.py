
from django.contrib import admin
from django.urls import path
from .myapp import views



urlpatterns = [
    path('<int:id>/', views.detail, name="detail"),
    path('index/', views.index,name='index'),
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('tv/',views.tv, name='tv'),
    path('laptops/', views.laptops, name='laptops'),
    path('phones/', views.phones, name='phones'),
    path('watches/', views.watches, name='watches'),
    path('basked/', views.basked, name='basked'),
    path('check/', views.check, name='check'),
]


