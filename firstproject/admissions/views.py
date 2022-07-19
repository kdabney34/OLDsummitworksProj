from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def addAdmission(request):
    # lets create a form and render it
    # let user fill it out and then we take it and submit a post request with it

    return HttpResponse('This is add admissions view')

def admissionsReport(request):
    return HttpResponse('This is admissoins report view')
