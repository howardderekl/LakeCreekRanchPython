from django.db import models
from .const import SaleStatus
from .lot import Lot

class HomeForSale(models.Model):
    """Homes for Sale Model"""
    class Meta:
        verbose_name_plural = 'Homes For Sale'
    description = models.TextField()
    address = models.CharField(max_length=100)
    mls_url = models.URLField()
    total_sqr_feet = models.IntegerField()
    bedroom_count = models.IntegerField()
    bathroom_count = models.DecimalField(max_digits=3, decimal_places=2)
    hide_from_website = models.BooleanField(default=False)
    completion_date = models.DateField()
    sale_status = models.IntegerField(default=SaleStatus.FOR_SALE, choices=SaleStatus.CHOICES)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    def __str__(self):
        return "HomeId: {0} @ {1}".format(self.id, self.address)
