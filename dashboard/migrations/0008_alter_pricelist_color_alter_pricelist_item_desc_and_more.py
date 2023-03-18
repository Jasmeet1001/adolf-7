# Generated by Django 4.1.6 on 2023-03-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_rename_product_pricelist_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='item_desc',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='mrp_incl_gst_pu',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_aft_gst_pu',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_bef_gst',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_bef_gst_pu',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_pernos_incl_gst',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='product_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='tax_rate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='unit_per_nos',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='uom',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='vehical_type',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
