# Generated by Django 4.0.8 on 2023-01-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_catalog_products_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='nazev',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
