# Generated by Django 4.0.8 on 2023-01-15 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='products_ids',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
