from django.contrib import admin
from .models import Part


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "catalog_number",
        "nom_number",
        "name",
        "price",
        "brand",
        "model",
        "unit",
        "months_without_movement",
    )

    search_fields = ("catalog_number", "nom_number", "name")
    ordering = ("number",)
