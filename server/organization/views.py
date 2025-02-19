from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Organization
from .serializers import OrganizationSerializer

# Create your views here.

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        queryset = Organization.objects.all()
        tech_stack = self.request.query_params.get('tech_stack', None)
        if tech_stack is not None:
            queryset = queryset.filter(tech_stack__icontains=tech_stack)
        return queryset

    @action(detail=False, methods=['get'])
    def tech_stacks(self, request):
        # Get unique tech stacks
        tech_stacks = Organization.objects.values_list('tech_stack', flat=True).distinct()
        return Response(list(tech_stacks))
