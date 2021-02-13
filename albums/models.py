from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #image_url=models.CharField(max_length=200)

    def __str__(self):
        return self.title
class Photo(models.Model):
    image_url= models.ForeignKey(Album,on_delete=models.CASCADE)
    description = models.TextField()
    datetime = models.DateTimeField()
    def __str__(self):
        return self.image_url