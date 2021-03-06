# Generated by Django 3.0.8 on 2020-07-04 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_item_probability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='item',
            name='probability',
            field=models.CharField(choices=[('rare', 'RARE'), ('low', 'LOW'), ('medium', 'Medium'), ('high', 'HIGH'), ('extreme', 'EXTREME')], default='normal', max_length=50),
        ),
    ]
