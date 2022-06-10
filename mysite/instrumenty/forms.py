from django import forms

class Form(forms.Form):
 ocena = forms.CharField(max_length=200)
