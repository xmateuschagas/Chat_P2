from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListView.as_view(), name='carro_list'),
    path('create/', views.carro_create, name='carro_create'),
    path('update/<int:pk>/', views.carro_update, name='carro_update'),
    path('delete/<int:pk>/', views.carro_delete, name='carro_delete'),
    path('register/', views.register, name='register'),  # URL para registro
]
