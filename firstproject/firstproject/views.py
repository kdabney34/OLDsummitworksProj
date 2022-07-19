from django.http import HttpResponse

def HomePage(request):
    return HttpResponse('this is our home page')
