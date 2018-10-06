from django.db import models
from datetime import timezone

# Create your models here.
class UserInfo(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    repass = models.CharField(max_length=50)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class contactInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to = 'picture/', default = 'picture/image.jpg')