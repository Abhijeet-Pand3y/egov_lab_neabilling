from django.shortcuts import render

# Create your views here.

def demand_type_form(request):
    return render(request, "demandType.html")