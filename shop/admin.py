from django.contrib import admin
from shop.models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProductSizeLetter)
class ProductSizeLetterAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ProductSizeNumerical)
class ProductSizeNumericalAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Product)
class ProductMenAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'discounted_price']
    list_filter = ['category', 'brand']
    search_fields = ['title']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'surname', 'name', 'street', 'house', 'payment']
    list_filter = ['status', 'payment']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']


@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ['reason']


@admin.register(Brand)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ['title']