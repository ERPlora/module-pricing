from django.urls import path
from . import views

app_name = 'pricing'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('pricelists/', views.price_lists_list, name='pricelists'),
    path('rules/', views.dashboard, name='rules'),


    # PriceList
    path('price_lists/', views.price_lists_list, name='price_lists_list'),
    path('price_lists/add/', views.price_list_add, name='price_list_add'),
    path('price_lists/<uuid:pk>/edit/', views.price_list_edit, name='price_list_edit'),
    path('price_lists/<uuid:pk>/delete/', views.price_list_delete, name='price_list_delete'),
    path('price_lists/<uuid:pk>/toggle/', views.price_list_toggle_status, name='price_list_toggle_status'),
    path('price_lists/bulk/', views.price_lists_bulk_action, name='price_lists_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
