from django.db import models

# Create your models here.

class Article(models.Model):
    head = models.CharField(max_length=100)
    text = models.CharField(max_length=2000)
    date = models.DateTimeField(null=True,blank=True)
    image = models.FileField(null=True, blank=True)
    def __str__(self) -> str:
        return self.head
    def month(self):
        return self.date.strftime('%B')

class Interview(models.Model):
    head = models.CharField(max_length=100)
    date = models.DateTimeField(null=True,blank=True)
    link = models.CharField(max_length=50)
    image = models.FileField(null=True, blank=True)
    def __str__(self) -> str:
        return self.head
    def month(self):
        return self.date.strftime('%B')