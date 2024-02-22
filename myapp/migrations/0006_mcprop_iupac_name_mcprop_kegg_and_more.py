# Generated by Django 5.0.1 on 2024-02-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_mcprop_molprot_mcprop_chembl_mcprop_pubchem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcprop',
            name='iupac_name',
            field=models.CharField(blank=True, default='Not available', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mcprop',
            name='kegg',
            field=models.CharField(blank=True, default='Not available', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='mcprop',
            name='molecular_formula',
            field=models.CharField(blank=True, default='Not available', max_length=255, null=True),
        ),
    ]