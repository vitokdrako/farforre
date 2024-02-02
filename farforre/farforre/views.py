from django.shortcuts import render, get_object_or_404
from .models import Product, ProductVariant
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

def gallery(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def rules(request):
    return render(request, 'rules.html')

def favorites(request):
    return render(request, 'favorites.html')

def search(request):
    return render(request, 'search.html')

def cart(request):
    return render(request, 'cart.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def get_variant(request):
    variant_id = request.GET.get('variant_id')
    variant = ProductVariant.objects.get(id=variant_id)
    data = {
        'price': variant.price,
        'availability': variant.availability,
        
    }
    return JsonResponse(data)