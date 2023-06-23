from django.db import models


from branch.models import Branch
# Create your models here.

class Customer(models.Model):

    sc_no = models.IntegerField()
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    date_of_birth = models.DateField()
    
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    demand = models.ForeignKey('demand.DemandType', on_delete=models.CASCADE)

    def __str__(self):
        return f"sc_no:{self.sc_no} Name: {self.full_name}"
    

