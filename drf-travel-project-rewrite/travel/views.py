from rest_framework import viewsets
from travel.models import TravelProject
from travel.serializers import TravelProjectSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer