# Generated by Django 3.2.5 on 2021-12-04 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('3', 'bepul'), ('2', 'ishlatilgan'), ('1', 'yangi')], default='1', max_length=10, null=True),
        ),
    ]
