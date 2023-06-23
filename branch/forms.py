from django import forms

class Branch(forms.Form):
    name = forms.CharField(label="branch_name", max_length=100)
    status = forms.BooleanField(label="")