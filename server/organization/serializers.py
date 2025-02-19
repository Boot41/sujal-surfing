from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name', 'tech_stack', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
