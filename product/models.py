from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="products")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()

class Billing(models.Model):
    fname=models.CharField(max_length=40)
    address=models.CharField(max_length=60)
    pincode=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    mobile=models.CharField(max_length=40)


    def __str__(self):
        return self.fname + " " + self.city
    

class Rating(models.Model):
    appuser=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.CharField(max_length=60)
    fav=models.CharField(max_length=60)
    feedback=models.CharField(max_length=60)
    
    
class Footwear(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="footwear")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()

class Shoe(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="shoe")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()


class Shirt(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="shirt")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()

class Croptop(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="shirt")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()

class Tshirt(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="shirt")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()

class Aline(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="shirt")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()

class Bodycon(models.Model):
    name=models.CharField(max_length=40)
    image=models.ImageField(upload_to="shirt")
    desc=models.TextField()
    price=models.FloatField()
    available=models.IntegerField()


