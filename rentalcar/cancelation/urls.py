from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CancellationViewSet

router = DefaultRouter()
router.register(r'cancelation', CancellationViewSet, basename='cancelation')  # 'cancelation' is the endpoint

urlpatterns = [
    path('', include(router.urls)),  # this will include all the URLs for the viewset
]
