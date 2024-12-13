from django.contrib import admin
from .models import RepairRequest
# Register your models here.

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
