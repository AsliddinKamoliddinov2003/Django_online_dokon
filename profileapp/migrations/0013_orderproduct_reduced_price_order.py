# Generated by Django 3.2.5 on 2021-12-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0012_remove_orderproduct_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='reduced_price_order',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
