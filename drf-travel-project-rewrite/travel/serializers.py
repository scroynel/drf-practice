from rest_framework import serializers, exceptions
from travel.models import TravelProject, TravelProjectPlace


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


class TravelProjectPlaceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelProjectPlace
        fields = ('notes', 'visited')