from django.db import models
from customer.models import Customer
from demand.models import DemandRate, DemandType

year_choice = (
    ('2080', '2080'),
    ('2079', '2079'),
    ('2078', '2078'),
    ('2077', '2077'),
    ('2076', '2076'),
    ('2075', '2075'),
    ('2074', '2074'),
    ('2073', '2073'),
    ('2072', '2072'),
    ('2071', '2071'),
    ('2070', '2070'),
    ('2069', '2069'),
    ('2068', '2068'),
    ('2067', '2067'),
    ('2066', '2066'),
    ('2065', '2065'),
    ('2064', '2064'),
    ('2063', '2063'),
    ('2062', '2062'),
    ('2061', '2061'),
    ('2060', '2060'),
    ('2059', '2059'),
)

month_choice = (
    ('Baisakh','Baisakh'),
    ('Jestha','Jestha'),
    ('Ashar','Ashar'),
    ('Sharawan','Sharawan'),
    ('Bhadra','Bhadra'),
    ('Aswin','Aswin'),
    ('Kartik','Kartik'),
    ('Mansir','Mansir'),
    ('Poush','Poush'),
    ('Magh','Magh'),
    ('Falgun','Falgun'),
    ('Chaitra','Chaitra'),
)
# Create your models here.


class Bill(models.Model):
    bill_date = models.DateField()
    bill_year = models.CharField(max_length=25, choices=year_choice)
    bill_month = models.CharField(max_length=12, choices=month_choice)

    current_reading = models.FloatField()
    prev_reading = models.FloatField()
    bill_amount = models.FloatField(blank=True)
    payment_status = models.BooleanField(default=False)

    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id} Name:{self.customer.full_name} Year:{self.bill_year} Month: {self.bill_month}"


    def save(self):
        cus = Customer.objects.get(pk = self.customer.id)
        demand_id = cus.demand

        demand_type_obj = DemandType.objects.get(pk = demand_id.id)

        demand_rate_obj = DemandRate.objects.get(demand_type = demand_type_obj.id)

        rate = demand_rate_obj.demand_rate

        self.bill_amount =  (self.current_reading - self.prev_reading) * rate/100
        

        super(Bill, self).save()