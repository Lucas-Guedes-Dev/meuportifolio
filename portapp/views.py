from typing import Any
from django.shortcuts import render
from django.views.generic import View
from .forms import LeadForm

class Index(View):
    def as_view(self, request):
        return render(request, 'components/home.html')
    
class Contato(View):
    def as_view(self, request):

        if request.method == 'POST':
            form = LeadForm(request.POST)

            if form.is_valid():
                
                obj = form.save(commit=True)
                
                obj.save()
        else:
            form = LeadForm()

        context = {'form' : form}

        return render(request, 'components/contato.html', context)