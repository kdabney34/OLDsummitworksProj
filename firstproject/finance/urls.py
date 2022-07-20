from django.contrib import admin
from django.urls import path
from finance.views import feeCollectionReport
from finance.views import feeDuesReport
from finance.views import feeCollection

urlpatterns = [

    path('feecoll/', feeCollection),
    path('duesreport/', feeDuesReport),
    path('collectionsreport/', feeCollectionReport),
]

