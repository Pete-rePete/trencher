# Generated by Django 3.0.4 on 2020-04-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0004_default_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='recipe_url',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
