from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Customer
from bill.models import Bill
from payment.models import Payment
from django.contrib.admin.views.decorators import user_passes_test
from .forms import CustomerForm
# Create your views here.

def customer_search(request):
    
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            mobile_no = request.POST['mobile_no']
            date_of_birth = request.POST['date_of_birth']
            try:
                customer = Customer.objects.get(mobile_no = mobile_no, full_name = name, date_of_birth = date_of_birth)
                bills = Bill.objects.filter(customer_id = customer.id)
                payments = Payment.objects.filter(bill__in=bills)



                return render(request, 'customerbill.html', {"customer":customer, "bills":bills, "payments":payments})
            except:
                return HttpResponse("Invalid Customer")
    else:
        form = CustomerForm()
    
    return render(request, 'customersearch.html', {"form": form})