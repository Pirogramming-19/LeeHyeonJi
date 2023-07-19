from django.db import models

class Devtool(models.Model):
    name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
    content = models.TextField()

class Idea(models.Model):
    # 아이디어명, 이미지, 아이디어 설명, 아이디어 관심도, 예상 개발툴
    title = models.CharField(max_length=30)
    image = models.FileField()
    content = models.TextField()
    interest = models.IntegerField()
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name='idea')