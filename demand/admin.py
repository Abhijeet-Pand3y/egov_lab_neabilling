from django.contrib import admin
from .models import DemandType,DemandRate

model_list = [DemandType, DemandRate]
# Register your models here.

admin.site.register(model_list)