# Generated by Django 5.0.1 on 2024-02-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_mcprop_num_hydro_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcprop',
            name='shape_complexity',
            field=models.CharField(blank=True, default='Not available', max_length=255, null=True),
        ),
    ]
