from django.shortcuts import render
from .forms import NameForm
from django.views.decorators.http import require_http_methods
from customer.models import Customer
from .models import Bill
from payment.models import Payment
from django.contrib.admin.views.decorators import user_passes_test

# @require_http_methods(['POST'])
@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
def search_user(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            customers = Customer.objects.filter(full_name=name)
            return render(request, 'customerdisplay.html', {"customers": customers})
    else:
        form = NameForm()
    
    return render(request, 'adminsearch.html', {"form": form})


@user_passes_test(lambda u: u.is_superuser, login_url='/admin/login/')
def display_users_bill(request, id):
    customer = Customer.objects.get(pk=id)
    bills = Bill.objects.filter(customer_id = id)
     
    payments = Payment.objects.filter(bill__in=bills)


    return render(request, 'displaybill.html', {"customer":customer, "bills":bills, "payments":payments})

