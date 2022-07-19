from django.http import HttpResponse
from django.shortcuts import render
from admissions.models import Admission
from django.views.generic.list import ListView

class HomePage(ListView):
    Model = Admission
    #querySet = Admission.objects.all()
    template_name = "Home-HomePage"
    context_object_name = 'adms'
    #return render(request, "Home-HomePage.html", {"admsList" : querySet})


