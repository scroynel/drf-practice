from rest_framework import serializers, exceptions
from travel.models import TravelProject, TravelProjectPlace, Place
from travel.partials.artic import fetch_data_place_api


class TravelProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = TravelProject
        fields = ('id', 'name', 'description', 'start_date', 'created_at')


class TravelProjectPlaceSerializer(serializers.ModelSerializer):
    external_id = serializers.IntegerField(write_only=True)

    class Meta: 
        model = TravelProjectPlace
        fields = '__all__'
        read_only_fields = ('project', 'place')


    def create(self, validated_data):
        project_pk = self.context['project_pk']
        project = TravelProject.objects.get(pk=project_pk)

        external_id = validated_data['external_id']
        place = Place.objects.filter(external_id=external_id)

        if not place:
            response = fetch_data_place_api(external_id)

            if not response:
                raise exceptions.ValidationError(f'Place {external_id} not found in external API')

            place = Place.objects.create(
                external_id = external_id,
                name = response['data']['title']
            )

        if TravelProjectPlace.objects.filter(project=project, place=place).exists():
            raise exceptions.ValidationError(f'This place {place.name} is already in the project')

        project_place = TravelProjectPlace.objects.create(
            project = project,
            place = place,
            notes = validated_data['notes'],
            visited = validated_data['visited']
        )

        return project_place


class TravelProjectPlaceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelProjectPlace
        fields = ('notes', 'visited')