import json
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product, ProductVariant, Cart, CartItem, User, Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    cart_items = CartItem.objects.filter(cart__customer=request.user.customer)
    total_price = sum(item.variant.price * item.quantity for item in cart_items)  # Використання price з ProductVariant
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

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

@receiver(post_save, sender=User)
def create_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_customer(sender, instance, **kwargs):
    instance.customer.save()

@require_POST
@csrf_exempt
def add_to_cart_ajax(request):
    data = json.loads(request.body.decode('utf-8'))
    variant_id = data.get('variant_id')  # Змінено з product_id на variant_id
    variant = get_object_or_404(ProductVariant, pk=variant_id)  # Отримання варіанту продукту
    cart, created = Cart.objects.get_or_create(customer=request.user.customer)
    cart_item, created = CartItem.objects.get_or_create(variant=variant, cart=cart, defaults={'quantity': data.get('quantity', 1)})
    
    if not created:
        cart_item.quantity += int(data.get('quantity', 1))
        cart_item.save()
    
    return JsonResponse({'message': 'Product variant added to cart successfully!'})

def get_cart_total(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer=customer, defaults={'total': 0})
        cart_items = CartItem.objects.filter(cart=cart)
        cart_total = sum(item.quantity for item in cart_items)
    else:
        cart_total = 0
    return JsonResponse({'cart_total': cart_total})