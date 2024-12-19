from django.urls import path
from . import views
from .views import ExchangeListView, ExchangeDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit_language, name='edit_language'),
    path('delete/<int:id>/', views.delete_language, name='delete_language'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_exchange/', views.add_exchange, name='add_exchange'),
    path('exchange_list/', views.exchange_list, name='exchange_list'),
    path('exchanges/', ExchangeListView.as_view(), name='exchange_list'),
    path('exchanges/<int:pk>/', ExchangeDetailView.as_view(), name='exchange_detail'),
]
