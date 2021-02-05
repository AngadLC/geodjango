from django.db import models
from django.contrib.gis.db import models as model_gis
# Create your models here.
class Nepal(models.Model):
    gid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    dcode = models.IntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=18, blank=True, null=True)
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    code1 = models.SmallIntegerField(blank=True, null=True)
    geom = model_gis.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nepal'
    def __str__(self):
        return self.dist_name

class pointdata(models.Model):
    name = models.CharField(max_length=50)
    geom = model_gis.PointField()
