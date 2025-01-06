from django import forms

class Buyer(forms.Form):
    name = forms.CharField()
    balance = forms.DecimalField()
    age = forms.CharField()