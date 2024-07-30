from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from .forms import LeadForm


class Index(View):
    def as_view(self, request):
        return render(request, 'components/home.html')


class Contato(View):
    def as_view(self, request):
        if request.method == 'POST':
            form = LeadForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Formulário salvo com sucesso!')
                # Redirecionar para a mesma página para evitar o reenvio do formulário
                return redirect('contato')
        else:
            form = LeadForm()

        context = {'form': form}
        return render(request, 'components/contato.html', context)
