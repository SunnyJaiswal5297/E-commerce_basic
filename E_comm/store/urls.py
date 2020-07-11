from django.urls import path
from . import views

urlpatterns = [
    #empty string for base
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
]