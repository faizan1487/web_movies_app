from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # imgPath = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/',null=True,blank=True)  # Use ImageField instead of FileField
    duration = models.IntegerField()
    language = models.CharField(max_length=50)
    userRating = models.IntegerField()
    genre = models.CharField(max_length=100)
    mpaaRatingType = models.CharField(max_length=10)
    mpaaRatingLabel = models.CharField(max_length=100)

    def __str__(self):
        return self.name
