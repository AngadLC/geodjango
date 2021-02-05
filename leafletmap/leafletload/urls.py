
from django.urls import path
from .views import index, nepal, pointdatafun,data
urlpatterns = [
    path('', index, name='index'),
    path('nepal',nepal, name = 'nepaldata'),
    path('pointdatafun',pointdatafun, name = 'pointdatafun'),
    path('data',data, name = 'locationdata')
]