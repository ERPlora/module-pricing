from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('pricelists/', views.pricelists, name='pricelists'),
    path('rules/', views.rules, name='rules'),
    path('settings/', views.settings, name='settings'),
]
