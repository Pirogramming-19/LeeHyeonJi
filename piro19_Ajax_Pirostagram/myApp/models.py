from django.db import models

class Post(models.Model):
    content = models.TextField()
    like = models.IntegerField()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comment')