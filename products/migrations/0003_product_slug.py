# Generated by Django 2.2.6 on 2019-12-20 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191220_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='abc'),
            preserve_default=False,
        ),
    ]