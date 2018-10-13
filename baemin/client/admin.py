from django.contrib import admin

# Register your models here.
from .models import Client,Order,OrderItem

# Register your models here.
@admin.register(Client,Order,OrderItem)
class ClientAdmin(admin.ModelAdmin):
    pass
