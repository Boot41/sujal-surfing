from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Q
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email', 'role']

    def get_queryset(self):
        queryset = Student.objects.all()
        role = self.request.query_params.get('role', None)
        if role is not None:
            queryset = queryset.filter(role=role.upper())
        return queryset

    @action(detail=False, methods=['get'])
    def roles(self, request):
        # Get count of students by role
        role_counts = Student.objects.values('role').annotate(count=Count('id'))
        return Response(role_counts)

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            queryset = Student.objects.filter(
                Q(name__icontains=query) |
                Q(email__icontains=query) |
                Q(role__icontains=query)
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response([])
