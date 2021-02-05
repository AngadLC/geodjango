from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.http import HttpResponse 
from .models import Nepal, pointdata
from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.geos import GEOSGeometry
from django.views import generic
from django.contrib.gis.db.models.functions import Distance
# Create your views here.

def nepal(request):
    nepaldata = serialize('geojson', Nepal.objects.all())
    return HttpResponse(nepaldata, content_type='geojson')


def index(request):
    return render(request, 'index.html')

def pointdatafun(request) : 
    try:
        data = request.GET #getting the data using the get request
        print(data)
        lat = data['lat2']
        lng = data['lng3']
        print(lat)
        location = fromstr(f'POINT({lng} {lat})', srid=4326)
        print(location)
        # save to the database
        obj = pointdata.objects.create(name=data['name1'],geom= location)
        if obj:
            return redirect('/')
        return HttpResponse("i get the data")
        # return "Success" 200
    except ValueError:
        error('Unable to parse JSON data from request.')
        # return "Error" 400
        return HttpResponse("i  frek out")

def data(request):
    data = serialize('geojson', pointdata.objects.all())
    return HttpResponse(data, content_type='geojson')

