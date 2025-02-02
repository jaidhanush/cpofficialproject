from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AvailabilityViewSet

router=DefaultRouter()
router.register('',AvailabilityViewSet,basename='availability')
app_name='availability'


urlpatterns = [
    path('',include(router.urls))
]
