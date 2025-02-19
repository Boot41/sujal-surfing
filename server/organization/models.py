from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=200)
    tech_stack = models.CharField(max_length=200)  # e.g., "Web Development", "Mobile Development", "Data Science"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.tech_stack}"

    class Meta:
        ordering = ['-created_at']
