from django.contrib import admin
from .models import Payment, PaymentOption
# Register your models here.

model_list = [Payment, PaymentOption]

admin.site.register(model_list)
