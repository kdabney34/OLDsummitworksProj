from django.http import HttpResponse
from django.shortcuts import render
#from django.views.generic.list import ListView

# I see you have been wondering what to render for home page. Generally it's the landing page for any web application. You can have a classbased view inheritaed from base class 'TemplateView'
# which basically takes a template_name that will have a welcome message and all the navigation links for web application 


#class HomePage(ListView):
#    model = Admission
#    #querySet = Admission.objects.all()
#    template_name = "Home-HomePage.html"
#    context_object_name = 'adms'
   
#    #return render(request, "Home-HomePage.html", {"admsList" : querySet})



#class HomePage(ListView):
#    model = Admission
#    #querySet = Admission.objects.all()
#    template_name = "Home-HomePage.html"
#    context_object_name = 'adms'
   
#    #return render(request, "Home-HomePage.html", {"admsList" : querySet})
