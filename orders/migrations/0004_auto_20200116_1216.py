# Generated by Django 2.2.8 on 2020-01-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_payment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('Card', 'Card'), ('Cash On Delivery', 'Cash On Delivery')], max_length=50, null=True),
        ),
    ]