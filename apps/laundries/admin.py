from django.contrib import admin
from .models import LaundryOrder, LaundryItem

# Register your models here.
@admin.register(LaundryOrder)
class LaundryOrderAdmin(admin.ModelAdmin):
    list_display = ('updated_at','customer', 'received_date', 'expected_completion_date', 'status')
    list_filter = ('customer', 'status')
    search_fields = ('customer', )

@admin.register(LaundryItem)
class LaundryItemAdmin(admin.ModelAdmin):
    list_display = ('updated_at','order', 'quantity', 'price_per_quantity', )
    search_fields = ('order', )