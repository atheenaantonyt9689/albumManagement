from django.db import models
from django.urls import reverse 

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def get_absolute_url(self): 
        return reverse('album-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title
class Photo(models.Model):
    image_url= models.CharField(max_length=200)
    description = models.TextField()
    posted_at = models.DateTimeField()
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_url

    def get_absolute_url(self): 
        return reverse('album-detail', args=[str(self.id)])