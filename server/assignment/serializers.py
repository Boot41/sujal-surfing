from rest_framework import serializers
from .models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'name', 'description', 'is_completed', 'assigned_date', 'due_date']
        read_only_fields = ['assigned_date']
