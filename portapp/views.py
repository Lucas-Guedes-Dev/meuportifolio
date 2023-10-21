from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LeadForm

class Index(View):
    def __init__(self):
        self.lead_form = LeadForm()

    def as_view(self, request):

        if request.method == 'POST':
            form = self.lead_form(request.POST)

            if form.is_valid():
                obj = form.save(commit=True)
                
                obj.save()
        else:
            form = self.lead_form

        context = {'form' : form}

        return render(request, 'components/home.html', context)