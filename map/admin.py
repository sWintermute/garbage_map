from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.widgets import AutocompleteSelect

from .models import Customer
from .models import Unit

from django import forms


class UnitAdmin(admin.ModelAdmin):
    list_display = ("district", "address", "n_mt")
    list_display_links = ("n_mt",)
    search_fields = ("n_mt", "district", "address")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","district", "street", "building", "corpus", "unit")
    list_display_links = ("id","unit",)
    search_fields = ("unit__n_mt", "street", "district")
    autocomplete_fields = [
        "unit",
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Unit, UnitAdmin)
