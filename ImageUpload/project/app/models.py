from django.db import models

# Create your models here.
class Imagedata(models.Model):
    Imagename=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="pics/")