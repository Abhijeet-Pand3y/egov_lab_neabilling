from django.shortcuts import render, HttpResponse, redirect
from .models import Payment, PaymentOption
from bill.models import Bill
from django.conf import settings
from django.contrib import messages
import requests
import aiohttp
import datetime
from django.http import JsonResponse
# Create your views here.

def payment_detail(request, id):
    payment = Payment.objects.filter(bill_id = id)
    
    return render(request, 'paymentdetails.html', {'payments':payment})

def payment(request, id):
    bill = Bill.objects.filter(pk = id)
    option = PaymentOption.objects.filter()
    return render(request, 'unpaidpayments.html', {'bills':bill, "options":option})


def khalti_payment_verify(request):
    token = request.GET.get('token')
    amount = request.GET.get('amount')
    bill_id = request.GET.get('bill_id')
    payload = {
        "token":token,
        "amount":amount,
    }
    headers = {
        "Authorization": "Key {}".format(settings.KHALTI_SECRET_KEY)
    }
    amount = int(amount)
    try:
        response = requests.post(settings.KHALTI_VERIFY_URL,payload,headers=headers)
        if response.status_code == 200 :
            bill = Bill.objects.get(pk = bill_id)
            bill.payment_status = True
            

            po = PaymentOption.objects.get(name="Khalti")
            payment = Payment(payment_date = datetime.datetime.now(), payment_amount = amount/100, bill=bill, payment_option = po)
            bill.save()
            payment.save()
 
            return JsonResponse({"Success": "Payment Success"})
            

        else:
            messages.success(request, "Bad Resposne could not verify payment")
            return JsonResponse({"Error": "Bad Resposne could not verify payment"})

    except Exception as e:
        return JsonResponse({"Error": e})
    
def message(request):
    messages.success(request, "Payment Success")
    return render(request, "paymentmessage.html")

