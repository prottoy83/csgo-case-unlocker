# Generated by Django 3.0.8 on 2020-07-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200703_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='probability',
            field=models.CharField(choices=[('low', 'LOW'), ('normal', 'NORMAL'), ('high', 'HIGH')], default='normal', max_length=50),
        ),
    ]
