from django.urls import path, include

from .views import VideoViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('videos', VideoViewSet, basename='video')


urlpatterns = [
    path('', include(router.urls))
]

