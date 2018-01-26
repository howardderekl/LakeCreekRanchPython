from django.db import models


class DevelopmentPhase(models.Model):
    """DevelopmentPhase Model to put Lots on"""
    name = models.CharField(max_length=250)
    start_date = models.DateField()
    complete_date = models.DateField()
    hide_from_website = models.BooleanField()

    def __str__(self):
        return "%s" % self.name
