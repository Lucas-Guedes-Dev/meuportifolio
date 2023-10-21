from django import forms

class LeadForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    empresa = forms.CharField(label='Empresa')