from django.db import models

# Create your models here.
class RepairRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[
        ('plumbing', 'Plumbing'),
        ('electrical', 'Electrical'),
        ('joiner', 'Joiner'),
        ('decorator', 'Painter and Decorator'),
        ('other', 'Other')
    ])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"
