from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Assignment
from .serializers import AssignmentSerializer

# Create your views here.

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    @action(detail=True, methods=['post'])
    def toggle_completion(self, request, pk=None):
        assignment = self.get_object()
        assignment.is_completed = not assignment.is_completed
        assignment.save()
        serializer = self.get_serializer(assignment)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Assignment.objects.all()
        completed = self.request.query_params.get('completed', None)
        if completed is not None:
            queryset = queryset.filter(is_completed=completed.lower() == 'true')
        return queryset
