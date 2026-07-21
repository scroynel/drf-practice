from django.db import models


class TravelProject(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Place(models.Model):
    external_id = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100)


class TravelProjectPlace(models.Model):
    project = models.ForeignKey(TravelProject, on_delete=models.CASCADE, related_name='places')
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    visited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)