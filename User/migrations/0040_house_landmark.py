# Generated by Django 4.1.1 on 2022-10-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0039_house_bhk'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='landmark',
            field=models.CharField(default='Near Tonk Road', max_length=50),
        ),
    ]