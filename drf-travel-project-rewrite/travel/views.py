from rest_framework import viewsets, exceptions
from travel.models import TravelProject
from travel.serializers import TravelProjectSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()
    serializer_class = TravelProjectSerializer


    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.places.filter(visited=True).exists():
            raise exceptions.ValidationError(f'This travel project "{obj.name}" cannot be removed. It has visited places!')
        
        return super().destroy(request, *args, **kwargs)