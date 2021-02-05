from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Nepal, pointdata
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class NEPALAdmin(LeafletGeoAdmin):
    list_display = ['dist_name', 'dcode']
    list_filter = ['dist_name']
    list_editable = ['dcode']
admin.site.register(Nepal, NEPALAdmin)
#allowing access to admin to add location

@admin.register(pointdata)
class pointdataAdmin(OSMGeoAdmin):
    list_display = ('name', 'geom')