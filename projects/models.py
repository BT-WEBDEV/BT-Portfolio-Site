from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
         
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='projects')
    github = models.URLField(max_length=200, default="Enter Link Here", blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title