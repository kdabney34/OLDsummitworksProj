from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse


class addProduct(CreateView):
    model = Product
    # form_class = BlogForm
    fields = ['name', 'text'] #form
    template_name = 'shop/product_create'  # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('product_list') # reverse map a url -

#def listProducts(request):
#    return HttpResponse('here we see all products')


class listProducts(ListView):
    model = Product
    
    querySet = Product.objects.all()
    template_name = "shop/product_list.html"
    context_object_name = 'products'
   
    #return render(request, "Home-HomePage.html", {"admsList" : querySet})

    
class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'productdetail'# 'blog' 'object'{}

    
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'shop/product_delete.html'  # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('product_list') # reverse map a url -


class UpdateProduct(UpdateView):
    model = Product
    fields = ['name', 'text']
    template_name = 'shop/product_update.html'  # If not provided, searches for 'blog/blog_form.html'
    success_url = reverse_lazy('product_list')
