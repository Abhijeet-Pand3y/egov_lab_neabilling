from django.urls import path
from . import views

urlpatterns = [
    path("payment_detail/<int:id>", views.payment_detail, name="payment_detail"),
    path("payment/<int:id>", views.payment, name="payment"),
    path("message/", views.message, name="message"),
    path("khalti_payment_verify/", views.khalti_payment_verify, name="khalti_payment_verify"),   
]
