from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png',  blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:75]+'....'
