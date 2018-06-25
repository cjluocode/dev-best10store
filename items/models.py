from django.db import models

# Create your models here.
class SearchItem(models.Model):

    title = models.CharField(max_length=500)
    link  = models.CharField(max_length=500)
    rating = models.FloatField()
    rating_count = models.IntegerField()
    hotscore = models.IntegerField()
    image    = models.CharField(max_length=300)
    price    = models.IntegerField(null=True,blank=True)
    comment_url = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    query_word = models.CharField(max_length=100, null=True, blank=True)
    price    = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.title
