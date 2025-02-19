from django.core.management.base import BaseCommand
from django.utils import timezone
from organization.models import Organization
from student.models import Student
from assignment.models import Assignment
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Initialize sample data for the application'

    def handle(self, *args, **kwargs):
        # Create Organizations
        self.stdout.write('Creating organizations...')
        organizations = [
            Organization.objects.create(
                name='Tech Innovators',
                tech_stack='Web Development',
            ),
            Organization.objects.create(
                name='Data Analytics Pro',
                tech_stack='Data Science',
            ),
            Organization.objects.create(
                name='Mobile Masters',
                tech_stack='Mobile Development',
            ),
        ]

        # Create Students
        self.stdout.write('Creating students...')
        students = [
            Student.objects.create(
                name='John Doe',
                role='INTERN',
                email='john.doe@example.com',
                joined_date='2025-01-15',
            ),
            Student.objects.create(
                name='Jane Smith',
                role='TRAINEE',
                email='jane.smith@example.com',
                joined_date='2025-02-01',
            ),
            Student.objects.create(
                name='Mike Johnson',
                role='FULL_TIME',
                email='mike.j@example.com',
                joined_date='2024-12-01',
            ),
            Student.objects.create(
                name='Sarah Wilson',
                role='INTERN',
                email='sarah.w@example.com',
                joined_date='2025-02-10',
            ),
        ]

        # Create Assignments
        self.stdout.write('Creating assignments...')
        current_date = timezone.now()
        assignments = [
            Assignment.objects.create(
                name='Build REST API',
                description='Create a RESTful API using Django REST Framework',
                is_completed=True,
                due_date=current_date + timedelta(days=7),
            ),
            Assignment.objects.create(
                name='Frontend Development',
                description='Develop responsive UI using React',
                is_completed=False,
                due_date=current_date + timedelta(days=14),
            ),
            Assignment.objects.create(
                name='Database Design',
                description='Design and implement database schema',
                is_completed=False,
                due_date=current_date + timedelta(days=5),
            ),
            Assignment.objects.create(
                name='Mobile App Feature',
                description='Implement authentication in mobile app',
                is_completed=True,
                due_date=current_date + timedelta(days=10),
            ),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully initialized sample data'))
