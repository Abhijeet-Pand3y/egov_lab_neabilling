from django.db import models
from bill.models import Bill
# Create your models here.

payment_platforms = (
    ('cash','cash'),
    ('Khalti','Khalti'),
    ('eSewa','eSewa'),
    ('fone pay','fone pay'),
)

class PaymentOption(models.Model):
    name = models.CharField(max_length=100, choices=payment_platforms)
    status = models.BooleanField(default=0)
    
class Payment(models.Model):
    payment_date = models.DateField()
    payment_amount = models.IntegerField()
    rebeat_amount = models.IntegerField(default=0, blank=True)
    fine_amount = models.IntegerField(default=0, blank=True)

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    payment_option = models.ForeignKey(PaymentOption, on_delete=models.CASCADE)