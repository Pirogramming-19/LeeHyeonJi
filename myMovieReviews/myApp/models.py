from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=30)                     # 영화 제목
    release_year = models.IntegerField()                        # 개봉 년도
    genre = models.CharField(max_length=10)                     # 장르
    rate = models.DecimalField(max_digits=2, decimal_places=1)  # 별점