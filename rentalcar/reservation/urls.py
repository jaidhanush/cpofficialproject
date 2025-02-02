from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ReservationViewSet

router=DefaultRouter()
router.register('',ReservationViewSet,basename='reservation')
app_name='reservation'


urlpatterns = [
    path('',include(router.urls))
]
