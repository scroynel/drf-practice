from django.contrib import admin
from travel.models import TravelProject, Place, TravelProjectPlace


admin.site.register(TravelProject)
admin.site.register(Place)
admin.site.register(TravelProjectPlace)
