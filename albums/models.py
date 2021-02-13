from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
class Photo(models.Model):
    image_url= models.CharField(max_length=200)
    description = models.TextField()
    posted_at = models.DateTimeField()
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_url