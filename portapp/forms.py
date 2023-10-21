from django import forms
from .models import Pessoa

class LeadForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    empresa = forms.CharField(label='Empresa')
    telefone = forms.CharField(label='Telefone')
    ativo = forms.BooleanField(label="Posso entrar em contato?")

    class Meta:
        model = Pessoa 
        fields = ['nome', 'email', 'empresa', 'telefone', 'ativo'] 