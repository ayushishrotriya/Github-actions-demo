# Generated by Django 4.1.1 on 2022-10-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0027_alter_villas_bed'),
    ]

    operations = [
        migrations.AddField(
            model_name='villas',
            name='bath',
            field=models.IntegerField(default=6),
        ),
    ]