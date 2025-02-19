from django.db import models

# Create your models here.

class Assignment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    assigned_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    
    def __str__(self):
        return self.name
