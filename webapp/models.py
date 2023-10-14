from django.db import models
import datetime
# Create your models here.
class HashTag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    n_tweets = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class WordUsage(models.Model):
    hashtag = models.ForeignKey(HashTag, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    n_used = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class HashTagTimeStatus:
    hashtag = models.ForeignKey(HashTag, on_delete=models.CASCADE)
    n_tweets = models.IntegerField()
    date = models.DateField()
    n_positive = models.IntegerField()
    n_negative = models.IntegerField()
    top_country = models.CharField(max_length=50)
    