from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(WindowEfficiency)
admin.site.register(WallInsulationEfficiency)
admin.site.register(RoofInsulationEfficiency)
admin.site.register(FloorInsulationEfficiency)
admin.site.register(HouseHeatingMethodEfficiency)
admin.site.register(ApartmentHeatingMethodEfficiency)