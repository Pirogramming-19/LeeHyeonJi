from django.db import models

class Idea(models.Model):
    # 아이디어명, 이미지, 아이디어 설명, 아이디어 관심도, 예상 개발툴
    title = models.CharField(max_length=30)
    image = models.FileField()
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.CharField(max_length=20)