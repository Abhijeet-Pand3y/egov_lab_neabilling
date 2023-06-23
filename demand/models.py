from django.db import models

demand_desc = (
    ('5 Ampere', '5 Ampere'),
    ('15 Ampere', '15 Ampere'),
    ('50 Ampere', '50 Ampere'),
)


# Create your models here.
class DemandType(models.Model):

    description = models.CharField(max_length=50, choices = demand_desc)
    status = models.BooleanField(default=0)

    def __str__(self):
        return self.description

class DemandRate(models.Model):

    demand_rate = models.FloatField()
    effective_date = models.DateField()
    is_current = models.BooleanField(default=False)

    demand_type = models.ForeignKey(DemandType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.demand_rate}"