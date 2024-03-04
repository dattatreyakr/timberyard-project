from django.contrib import admin
from .models import woods, benifits, OrderConfirm


# Register your models here.
@admin.register(woods)
class woodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'amount', 'itemAdded')


@admin.register(benifits)
class benifitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fkey', 'benift')


@admin.register(OrderConfirm)
class orderConform(admin.ModelAdmin):
    list_display = (
    'id', 'date', 'email', 'address', 'city', 'pin', "phone", "totalc", "mode", "product", "product_id", "total_amount",
    "quantiy")
