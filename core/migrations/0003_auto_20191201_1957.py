# Generated by Django 2.2.4 on 2019-12-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191201_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('D', 'danger'), ('P', 'primary')], max_length=1),
        ),
    ]
