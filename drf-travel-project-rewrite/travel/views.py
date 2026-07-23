from rest_framework import viewsets, exceptions
from travel.models import TravelProject, TravelProjectPlace
from travel.serializers import TravelProjectSerializer, TravelProjectPlaceSerializer, TravelProjectPlaceUpdateSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer


    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.places.filter(visited=True).exists():
            raise exceptions.ValidationError(f'This travel project "{obj.name}" cannot be removed. It has visited places!')
        
        return super().destroy(request, *args, **kwargs)


class TravelProjectPlaceViewSet(viewsets.ModelViewSet):
    serializer_class = TravelProjectPlaceSerializer


    def get_queryset(self):
        project_pk = self.kwargs['project_pk']
        return TravelProjectPlace.objects.filter(project_id=project_pk)


    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return TravelProjectPlaceUpdateSerializer
        return TravelProjectPlaceSerializer