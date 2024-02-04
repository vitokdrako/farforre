from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва товару", blank=True, default='')
    article_number = models.CharField(max_length=50, verbose_name="Артикул", blank=True, default='')
    color = models.CharField(max_length=20, blank=True, verbose_name="Колір", default='')
    image = models.ImageField(upload_to='product_images/', verbose_name="Зображення")
    related_products = models.ManyToManyField('self', blank=True, verbose_name="Супутні товари")

    def __str__(self):
        return self.name
    
    
class ProductVariant(models.Model):
    SIZE_CHOICES = [
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
    ]
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, verbose_name="Розмір")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    availability = models.CharField(max_length=50, verbose_name="Наявність")
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Вага")
    damages = models.CharField(max_length=100, blank=True, verbose_name="Збитки")
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Висота")
    length = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Довжина")
    width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Ширина")
    diameter = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Діаметр")

    def __str__(self):
        return f"{self.product.name} - {self.size}"
    
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікування'),
        ('confirmed', 'Підтверджено'),
        ('shipped', 'Відправлено'),
        ('delivered', 'Доставлено'),
    ]
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product_variant or self.product_set} x {self.quantity}"
    