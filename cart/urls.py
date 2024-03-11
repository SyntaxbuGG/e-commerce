from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/', views.cart_add, name='cart_add'),
    path('shop/',views.cart_index, name='cart_shop'),
]
