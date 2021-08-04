from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Content(models.Model):
    para = models.TextField(blank=False, default="Kolawole is a programmer")
    para2 = models.TextField(blank=True)
    resume = models.FileField(blank=False)

    def __str__(self):
        return f"{self.para} {self.para2} {self.resume}"

class Project(models.Model):
    title = models.CharField(max_length=250, blank=True)
    picture = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    link = models.URLField(blank=True)
    source_code = models.URLField(blank=True)
    tools = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.title} {self.picture} {self.description} {self.link} {self.source_code} {self.tools}"