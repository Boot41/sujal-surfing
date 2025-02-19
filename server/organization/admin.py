from django.contrib import admin
from .models import Organization

# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'tech_stack', 'created_at', 'updated_at')
    list_filter = ('tech_stack', 'created_at')
    search_fields = ('name', 'tech_stack')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
