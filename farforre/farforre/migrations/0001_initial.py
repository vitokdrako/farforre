# Generated by Django 5.0.1 on 2024-02-04 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Очікування'), ('confirmed', 'Підтверджено'), ('shipped', 'Відправлено'), ('delivered', 'Доставлено')], default='pending', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='farforre.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, verbose_name='Назва товару')),
                ('article_number', models.CharField(blank=True, default='', max_length=50, verbose_name='Артикул')),
                ('color', models.CharField(blank=True, default='', max_length=20, verbose_name='Колір')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='Зображення')),
                ('related_products', models.ManyToManyField(blank=True, to='farforre.product', verbose_name='Супутні товари')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=3, verbose_name='Розмір')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('availability', models.CharField(max_length=50, verbose_name='Наявність')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Вага')),
                ('damages', models.CharField(blank=True, max_length=100, verbose_name='Збитки')),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Висота')),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Довжина')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Ширина')),
                ('diameter', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Діаметр')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='farforre.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='farforre.order')),
                ('product_variant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='farforre.productvariant')),
            ],
        ),
    ]
