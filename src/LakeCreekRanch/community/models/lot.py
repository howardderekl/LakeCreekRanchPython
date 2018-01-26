from django.db import models
from .const import SaleStatus
from .developmentphase import DevelopmentPhase

class Lot(models.Model):
    """Lot Model to put homes on"""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    total_acres = models.DecimalField(max_digits=3, decimal_places=2)
    sale_status = models.IntegerField(default=SaleStatus.FOR_SALE, choices=SaleStatus.CHOICES)
    development_phase = models.ForeignKey(DevelopmentPhase, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name