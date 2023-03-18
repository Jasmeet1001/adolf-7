# Generated by Django 4.1.6 on 2023-03-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_pricelist_color_alter_pricelist_item_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricelist',
            name='color',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='item_desc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='mrp_incl_gst_pu',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_aft_gst_pu',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_bef_gst',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_bef_gst_pu',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='price_pernos_incl_gst',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='product_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='tax_rate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='unit_per_nos',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='uom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pricelist',
            name='vehical_type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
