from django.contrib import admin
from .models import Customer, Order, GunPart, Finish, Design

class GunPartInline(admin.TabularInline):
    model = GunPart
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_in', 'date_out', 'status')
    list_filter = ('status', 'date_in')
    search_fields = ('customer__name',)
    inlines = [GunPartInline]

@admin.register(GunPart)
class GunPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'part_type', 'finish', 'design')
    list_filter = ('part_type', 'finish')
    search_fields = ('name', 'serial_number')

@admin.register(Finish)
class FinishAdmin(admin.ModelAdmin):
    list_display = ('name', 'finish_type', 'color')
    search_fields = ('name', 'color', 'finish_type')

@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'design_type')
    search_fields = ('name', 'design_type')
