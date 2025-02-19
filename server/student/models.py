from django.db import models

# Create your models here.

class Student(models.Model):
    ROLE_CHOICES = [
        ('INTERN', 'Intern'),
        ('TRAINEE', 'Trainee'),
        ('FULL_TIME', 'Full Time'),
    ]

    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='TRAINEE')
    email = models.EmailField(unique=True)
    joined_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.role}"

    class Meta:
        ordering = ['-joined_date']
