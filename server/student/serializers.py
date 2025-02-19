from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'role', 'email', 'joined_date', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_email(self, value):
        # Convert email to lowercase before validation
        return value.lower()
