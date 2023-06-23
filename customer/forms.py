from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=20)
    date_of_birth = forms.DateField()
