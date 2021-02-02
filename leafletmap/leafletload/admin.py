from django.contrib import admin
from .models import Nepal
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class NEPALAdmin(LeafletGeoAdmin):
    list_display = ['dist_name', 'dcode']
    list_filter = ['dist_name']
    list_editable = ['dcode']


admin.site.register(Nepal, NEPALAdmin)
