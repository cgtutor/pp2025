from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return self.title