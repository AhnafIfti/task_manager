from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    status_options = (
        (1, "Pending"),
        (2, "In Progress"),
        (3, "Completed"),
    )

    status = models.IntegerField(choices=status_options)

    priority_options = (
        (1, "Low"),
        (2, "Medium"),
        (3, "High"),
    )

    priority = models.IntegerField(choices=priority_options)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title