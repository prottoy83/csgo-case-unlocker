# Generated by Django 3.0.8 on 2020-07-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200704_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='probability',
            field=models.CharField(choices=[('rare', 'Extreme Rare'), ('low', 'Rare'), ('medium', 'Medium'), ('high', 'Common'), ('extreme', 'Very Common')], default='normal', max_length=50),
        ),
    ]
