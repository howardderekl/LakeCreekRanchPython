from django.contrib import admin

from .models import DevelopmentPhase, Lot, HomeForSale

admin.site.register(DevelopmentPhase)
admin.site.register(Lot)
admin.site.register(HomeForSale)