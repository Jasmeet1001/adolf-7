from django.contrib import admin
from .models import AdolfAdmin, Retailer, Distributer, PriceList
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(PriceList)
class PriceListData(ImportExportModelAdmin):
    pass
admin.site.register(AdolfAdmin)
admin.site.register(Retailer)
admin.site.register(Distributer)
