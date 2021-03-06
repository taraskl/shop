# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-06-24 09:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='productinbasket',
            options={'verbose_name': 'Product In Basket', 'verbose_name_plural': 'Products In Basket'},
        ),
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product In Order', 'verbose_name_plural': 'Products In Order'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Order status', 'verbose_name_plural': 'Orders status'},
        ),
    ]
