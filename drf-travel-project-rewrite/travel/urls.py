from django.urls import path
from rest_framework import routers
from travel.views import TravelProjectViewSet


router = routers.SimpleRouter()
router.register('', TravelProjectViewSet)


urlpatterns = router.urls