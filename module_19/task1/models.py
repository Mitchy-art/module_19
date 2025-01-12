from django.db import models

# Create your models here.


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Games(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.CharField(max_length=500)
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Cats(models.Model):
    gender = models.CharField(max_length=6)
    breed = models.CharField(max_length=50)
    colors = models.CharField(max_length=100)
    age = models.CharField(max_length=5)