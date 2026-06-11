from django.urls import path
from . import views

urlpatterns = [
    path('', views.minha_view, name='home'),
    path('produtos/', views.produtos_view, name='produtos'),
    path('produtos2/', views.produtos_view2, name='produtos'),
]
