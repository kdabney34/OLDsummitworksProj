from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def feeCollection(request):
    return HttpResponse('i will collect the fee from this view')

def feeDuesReport(request):
    return HttpResponse('i will get dues report from this view')

def feeCollectionReport(request):
    return HttpResponse('i will get collection report from this view')
















