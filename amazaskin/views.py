from django.shortcuts import render
from .models import Product

# Create your views here.
def shop(request):

    products = Product.objects.all()
    
    context = {
        'products': products,
        'page_title': "Shop the Range",
    }

    return render(request, 'shop.html', context)