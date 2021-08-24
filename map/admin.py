from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Customer
from .models import Unit


class UnitAdmin(admin.ModelAdmin):
    list_display = ("district", "address", "n_mt")
    list_display_links = ("n_mt",)
    search_fields = ("n_mt", "district", "address")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("district", "street", "building", "corpus", "unit")
    list_display_links = ("unit",)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Unit, UnitAdmin)
