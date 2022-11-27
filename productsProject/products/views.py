from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from products.forms import RegisterForm

# Create your views here.

def home(request):
    return HttpResponse("weclome in products app")

def productDetails(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/productDetails.html", {"product": product})

def productsList(request):
    return render(request, "products/productsList.html", {"products": Product.objects.all()})

def userRegister(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = RegisterForm()
    return render(request, "products/userRegister.html", {"form": form})