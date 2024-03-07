# Generated by Django 5.0.1 on 2024-02-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_phytochemical_target_prop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phytochemical',
            name='target_prop',
        ),
        migrations.AddField(
            model_name='phytochemical',
            name='target_prop',
            field=models.ManyToManyField(blank=True, to='myapp.target'),
        ),
    ]
