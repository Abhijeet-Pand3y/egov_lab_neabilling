from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label="Enter Name:", max_length=100)