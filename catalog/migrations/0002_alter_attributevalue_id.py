# Generated by Django 4.0.8 on 2023-01-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributevalue',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
