from django.db import models
 

# Create your models here.
class Blog(models.Model):
    text=models.TextField(max_length=200)
    photo=models.ImageField(upload_to='img')

    def __str__(self):
        return self.text
    

