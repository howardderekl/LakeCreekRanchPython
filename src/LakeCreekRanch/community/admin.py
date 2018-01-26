from django.contrib import admin

from .models import DevelopmentPhase, Lot, HomeForSale

@admin.register(DevelopmentPhase)
class DevelopmentPhaseAdmin(admin.ModelAdmin):
    """Declaration of what to display for the DevelopmentPhases in the Admin Tool"""
    list_display = ('name',
                    'start_date',
                    'complete_date',
                    'hide_from_website')
    list_editable = ('hide_from_website',)

@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    """Declaration of what to display for the Lots in the Admin Tool"""
    list_display = ('name',
                    'description',
                    'total_acres',
                    'sale_status',
                    'development_phase')
    list_editable = ('sale_status',)

@admin.register(HomeForSale)
class HomeForSaleAdmin(admin.ModelAdmin):
    """Declaration of what to display for the HomesForSale in the Admin Tool"""
    list_display = ('id',
                    'address',
                    'total_sqr_feet',
                    'bedroom_count',
                    'bathroom_count',
                    'hide_from_website',
                    'completion_date',
                    'sale_status',
                    'lot')
    list_editable = ('hide_from_website', 'sale_status')
