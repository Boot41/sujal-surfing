from django.contrib import admin
from .models import Assignment

# Register your models here.

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_completed', 'assigned_date', 'due_date')
    list_filter = ('is_completed', 'assigned_date', 'due_date')
    search_fields = ('name', 'description')
    ordering = ('-assigned_date',)
    readonly_fields = ('assigned_date',)
    date_hierarchy = 'due_date'
    list_editable = ('is_completed',)  # Allow quick status updates
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Status', {
            'fields': ('is_completed', 'assigned_date', 'due_date')
        }),
    )
