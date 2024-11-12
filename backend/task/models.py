from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

