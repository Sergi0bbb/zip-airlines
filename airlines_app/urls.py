from django.urls import path, include
from rest_framework.routers import DefaultRouter
from airlines_app.views import AirplaneViewSet

app_name = "airlines_app"

router = DefaultRouter()
router.register("airplanes", AirplaneViewSet, basename="airplanes")

urlpatterns = [
    path("", include(router.urls)),
]
