from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CarViewSet

router=DefaultRouter()
router.register('',CarViewSet,basename='car')
app_name='car'


urlpatterns = [
    path('',include(router.urls))
]
