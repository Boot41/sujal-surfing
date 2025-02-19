from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'joined_date', 'created_at')
    list_filter = ('role', 'joined_date')
    search_fields = ('name', 'email')
    ordering = ('-joined_date',)
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'joined_date'  # Adds date-based navigation
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('email',)  # Make email readonly after creation
        return self.readonly_fields
