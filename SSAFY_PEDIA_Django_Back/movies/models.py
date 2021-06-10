from django.db import models
from django.conf import settings
# user
from django.core.validators import MinValueValidator, MaxValueValidator
# 별점 rank field 수치 최저 최고

class Mbti(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    vote_average = models.FloatField()
    mbti = models.CharField(max_length=100)
    # like_mbti_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_mbti_movies')
    # 좋아요 : mbti 영화 M:N 외래키 추가?
    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.CharField(max_length=100)
    vote_average = models.FloatField()
    genre = models.CharField(max_length=50)
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # 좋아요 : 영화 M:N 외래키

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    # user : 리뷰 1:N 외래키
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # 영화 : 리뷰 1:N 외래키
    # mbti_movie = models.ForeignKey(Mbti, on_delete=models.CASCADE)
    # mbti 영화 : 리뷰 1:N 외래키 추가? 역참조 이름 review_set 겹치지 않도록 related_name 설정 필요
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # 별점 숫자 (범위 정하기)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    # user : 댓글 1:N 외래키
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    # 리뷰 : 댓글 1:N 외래키
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content