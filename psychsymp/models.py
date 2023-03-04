from django.db import models

class Update(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    post = models.TextField()