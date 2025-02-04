from django.urls import path
from .views import book_car, cancel_booking, check_availability, reserve_car

urlpatterns = [
    path('book/', book_car, name='book_car'),
    path('cancel_booking/', cancel_booking, name='cancel_booking'),
    path('check_availability/', check_availability, name='check_availability'),
    path('reserve_car/', reserve_car, name='reserve_car'),
]
