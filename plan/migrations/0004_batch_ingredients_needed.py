# Generated by Django 3.0.4 on 2020-05-12 21:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_batch_meal_related_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='ingredients_needed',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None),
        ),
    ]
