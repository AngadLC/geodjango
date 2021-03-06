# Generated by Django 3.1.6 on 2021-02-02 10:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nepal',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.IntegerField(blank=True, null=True)),
                ('dcode', models.IntegerField(blank=True, null=True)),
                ('dist_name', models.CharField(blank=True, max_length=18, null=True)),
                ('shape_leng', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('shape_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('code1', models.SmallIntegerField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'nepal',
                'managed': False,
            },
        ),
    ]
