from django.db import models

# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length=100)
    link  = models.CharField(max_length=500)
    rating = models.FloatField()
    rating_count = models.IntegerField()
    hotscore = models.IntegerField()
    image    = models.CharField(max_length=300)
    price    = models.IntegerField()

    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):

        return self.title


