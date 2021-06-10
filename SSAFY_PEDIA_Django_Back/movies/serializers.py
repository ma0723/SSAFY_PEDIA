from rest_framework import serializers
from .models import Movie, Review, Comment, Mbti
# Mbti import

# 상세 리뷰 전체 댓글 조회(GET)
class CommentSerializer(serializers.ModelSerializer):
    review_title = serializers.SerializerMethodField()
    def get_review_title(self, obj):
        return obj.review.title
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
        return obj.user.username
    class Meta:
        model = Comment
        fields = ('id', 'userName', 'user', 'review', 'review_title', 'content', 'created_at',)
        read_only_fields = ('user','review',)
        # 작성 불요 (read_only_fields)

# 상세 영화 전체 리뷰 조회(GET)
class ReviewListSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    def get_movie_title(self, obj):
        return obj.movie.title
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
        return obj.user.username
    class Meta:
        model = Review
        fields = ('id', 'userName', 'user', 'movie_title', 'movie', 'title', 'content', 'rank', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'movie',)
        # 작성 불요 (read_only_fields)

# 상세 리뷰 조회(GET)
class ReviewSerializer(serializers.ModelSerializer):
    # comment_set = CommentSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 상세 리뷰에 대한 모든 코멘트 조회
    movie_title = serializers.SerializerMethodField()
    def get_movie_title(self, obj):
        return obj.movie.title
    userName = serializers.SerializerMethodField()
    def get_userName(self,obj):
        return obj.user.username
    class Meta:
        model = Review
        fields = ('id', 'userName', 'user', 'movie_title', 'movie', 'title', 'content', 'rank', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'movie',)
        # 작성 불요 (read_only_fields)

# 전체 영화 조회(GET)
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_user', 'like_movies')

# 상세 영화 조회 (GET)
class MovieSerializer(serializers.ModelSerializer):
    # review_set = ReviewSerializer(many=True, read_only=True),)
    # review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    # 상세 영화에 대한 모든 리뷰 조회
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_user', 'like_movies')

# 전체 mbti 추천 영화 조회(GET)
class MbtiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbti
        fields = '__all__'
        # read_only_fields = ('like_mbti_user', 'like_mbti_movies')

# 상세 mbti 추천 영화 조회(GET)
class MbtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbti
        fields = '__all__'
        # read_only_fields = ('like_mbti_user', 'like_mbti_movies')

