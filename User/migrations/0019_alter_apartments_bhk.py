# Generated by Django 4.1.1 on 2022-10-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0018_apartments_bhk_apartments_additionalroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartments',
            name='Bhk',
            field=models.IntegerField(default=2),
        ),
    ]
