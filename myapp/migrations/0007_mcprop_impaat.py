# Generated by Django 5.0.1 on 2024-02-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_mcprop_iupac_name_mcprop_kegg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcprop',
            name='impaat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]