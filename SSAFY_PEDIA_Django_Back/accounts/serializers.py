from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
# user get_user_model(models.py 외에 적용)
# user settings.AUTH_USER_MODEL(models.py)

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    # write_only : 시리얼라이징은 하지만 응답에는 포함시키지 않음
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'like_movies', 'reviews', 'comments',)
        # 유저 등록시 작성 필요 
        # 유저의 pk (id)
        # 좋아요한 영화(like_movies) 역참조
        # 작성한 리뷰(reviews) 역참조
        # 작성한 댓글(comments) 역참조
        read_only_fields = ('reviews', 'like_movies', 'comments',)
        # 유저 등록시 작성 불요
