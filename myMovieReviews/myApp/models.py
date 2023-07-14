from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=30)                     # 영화 제목
    release_year = models.IntegerField()                        # 개봉 년도
    genre = models.CharField(max_length=10)                     # 장르
    rate = models.DecimalField(max_digits=2, decimal_places=1)  # 별점
    running_time = models.IntegerField()                        # 러닝타임(단위 min)
    content = models.TextField()                                # 리뷰 내용
    director = models.CharField(max_length=20)                  # 영화 감독
    lead = models.CharField(max_length=100)                     # 주연 배우