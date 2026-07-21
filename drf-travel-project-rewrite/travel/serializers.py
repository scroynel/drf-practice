from rest_framework import serializers, exceptions
from travel.models import TravelProject


class TravelProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = TravelProject
        fields = ('id', 'name', 'description', 'start_date', 'created_at')