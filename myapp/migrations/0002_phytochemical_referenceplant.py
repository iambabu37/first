# Generated by Django 5.0.1 on 2024-02-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phytochemical',
            name='referenceplant',
            field=models.ManyToManyField(to='myapp.reference'),
        ),
    ]