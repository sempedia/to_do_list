from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    STATUS_CHOICES = (
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='incomplete')

    def __str__(self):
        return self.title
