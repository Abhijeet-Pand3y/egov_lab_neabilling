from django.contrib import admin
from .models import Bill
# Register your models here.

model_list = [Bill]

admin.site.register(model_list)
