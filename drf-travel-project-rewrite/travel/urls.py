from django.urls import path
from rest_framework import routers
from travel.views import TravelProjectViewSet, TravelProjectPlaceViewSet


router = routers.SimpleRouter()
router.register('projects', TravelProjectViewSet)


urlpatterns = [
    path('projects/<int:project_pk>/places/', TravelProjectPlaceViewSet.as_view({'get': 'list', 'put': 'update'}), name='project_places')
]

urlpatterns += router.urls