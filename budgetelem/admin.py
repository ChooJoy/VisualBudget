from budgetelem.models import BElem
from budgetelem.models import CodesProfit
from budgetelem.models import Document
from budgetelem.models import Region
from budgetelem.models import FedOkr
from budgetelem.models import EconOkr
from django.contrib import admin

#admin.site.register(FedOkr)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('authority_name', 'fed_region_local', 'region', 'year')

admin.site.register(Document, DocumentAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('code_rus', 'name','fedokr', 'econokr')
    ordering = ['code_rus']

admin.site.register(Region, RegionAdmin)


class FedOkrAdmin(admin.ModelAdmin):
    fields = ['name', 'center']
    list_display = ('name','center')

admin.site.register(FedOkr, FedOkrAdmin)

class EconOkrAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', )

admin.site.register(EconOkr, EconOkrAdmin)

#class CodesProfitAdmin(admin.ModelAdmin):
#    fields = ['code', 'name', 'deep']
#    list_display = ('code', 'deep', 'name')

#admin.site.register(CodesProfit, CodesProfitAdmin)
