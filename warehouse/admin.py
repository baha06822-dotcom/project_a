from django.contrib import admin
from .models import Warehouse, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active")
    search_fields = ("code", "name")
    list_filter = ("is_active",)


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "department", "is_active")
    search_fields = ("code", "name")
    list_filter = ("is_active", "department")