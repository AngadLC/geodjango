
from django.urls import path
from .views import index, nepal
urlpatterns = [
    path('', index, name='index'),
    path('nepal',nepal, name = 'nepaldata')
]