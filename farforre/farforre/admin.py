from django.contrib import admin
from .models import Product, ProductVariant
from django.urls import reverse
from django.utils.html import format_html
from .models import Customer, Order, OrderItem, ProductSet

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1  # Кількість початкових рядків для редагування

def dublicate_product(modeladmin, request, queryset):
    for product in queryset:
        product.id = None 
        product.save()
        
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'name', 'color', 'article_number', 'view_on_site_link')
    list_editable = ('name', 'article_number')
    list_display_links = ('preview_image',)
    search_fields = ('name', 'article_number', 'color')
    actions = [dublicate_product]
    filter_horizontal = ('related_products',)
    inlines = [ProductVariantInline]

    def view_on_site_link(self, obj):
        url = reverse('product_detail', kwargs={'pk': obj.pk})
        return format_html('<a href="{}" target="_blank">Перегляд</a>', url)

    view_on_site_link.short_description = 'Переглянути'

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 65px; height: 45px;" />', obj.image.url)
        return ""

    preview_image.short_description = 'Прев\'ю'
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address')
    # Додайте інші налаштування, які ви бажаєте

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at', 'status')
    list_filter = ('status',)
    # Додайте інші налаштування, які ви бажаєте

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_variant', 'product_set', 'quantity')
    # Додайте інші налаштування, які ви бажаєте

@admin.register(ProductSet)
class ProductSetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('products',)
    # Додайте інші налаштування, які ви бажаєте