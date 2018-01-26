from django.db import models

FOR_SALE_CHOICES = (
    ('F', 'For Sale'),
    ('S', 'Sold'),
    ('P', 'Sale Pending')
)

class DevelopmentPhase(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    complete_date = models.DateField()
    hide_from_website = models.BooleanField()

    def __str__(self):
        return "%s" % self.name


class Lot(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    total_acres = models.DecimalField(max_digits=3, decimal_places=2)
    sale_status = models.CharField(max_length=1, default='F',
                                    choices=FOR_SALE_CHOICES)
    development_phase = models.ForeignKey(DevelopmentPhase, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name


class HomeForSale(models.Model):
    description = models.TextField()
    address = models.CharField(max_length=100)
    mls_url = models.URLField()
    total_sqr_feet = models.IntegerField()
    bedroom_count = models.IntegerField()
    bathroom_count = models.DecimalField(max_digits=3, decimal_places=2)
    hide_from_website = models.BooleanField(default=False)
    completion_date = models.DateField()
    sale_status = models.CharField(max_length=1, default='F', choices=FOR_SALE_CHOICES)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    def __str__(self):
        return "HomeId: {0} @ {1}".format(self.id, self.address)