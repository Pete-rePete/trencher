# Generated by Django 3.0.4 on 2020-06-08 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0010_ingredient_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='deactivated',
            field=models.BooleanField(default=False),
        ),
    ]
