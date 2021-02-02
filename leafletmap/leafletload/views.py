from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Nepal

# Create your views here.

def nepal(request):
    nepaldata = serialize('geojson', Nepal.objects.all())
    return HttpResponse(nepaldata, content_type='geojson')


def index(request):
    return render(request, 'index.html')