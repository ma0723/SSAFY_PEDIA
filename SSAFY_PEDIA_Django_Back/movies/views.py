from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# 직렬화를 위한 데코레이터 (DRF)

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# TOKEN 유효여부와 인증을 위한 데코레이터 (JWT)

from .models import Movie, Review, Comment, Mbti
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer, MbtiListSerializer, MbtiSerializer
# models.py
# serializers.py

from django.contrib.auth import get_user_model

@api_view(['POST'])
def user_likes(request, user_pk):
# 사용자가 좋아요한 영화
  user = get_object_or_404(get_user_model(), pk=user_pk)
  # likes = user.like_movies.all()
  # 역참조(related name) like_movies
  data = []
  movies_pk = request.data
  for movie_pk in movies_pk:
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  return Response(data)

@api_view(['POST'])
def user_reviews(request, user_pk):
# 사용자가 생성한 리뷰 조회
  user = get_object_or_404(get_user_model(), pk=user_pk)
  # reviews = user.reviews.all()
  # 역참조(related name) reviews
  data = []
  reviews_pk = request.data
  for review_pk in reviews_pk:
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    data.append(serializer.data)
  return Response(data)

@api_view(['POST'])
def user_comments(request, user_pk):
# 사용자가 생성한 댓글 조회
  user = get_object_or_404(get_user_model(), pk=user_pk)
  # comments = user.comments.all()
  # 역참조(related name) comments
  data = []
  comments_pk = request.data
  for comment_pk in comments_pk:
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    data.append(serializer.data)
  return Response(data)

@api_view(['GET'])
def genre(request):
# 장르별 추천 영화 조회 (GET)
    action_movies = Movie.objects.filter(genre="액션")[:15]
    serializer1 = MovieListSerializer(action_movies, many=True)
    # 액션 영화 
    animation_movies = Movie.objects.filter(genre="애니메이션")[:15]
    serializer2 = MovieListSerializer(animation_movies, many=True)
    # 애니메이션 영화
    thriller_movies = Movie.objects.filter(genre="스릴러")[:15]
    serializer3 = MovieListSerializer(thriller_movies, many=True)
    # 스릴러 영화
    fantasy_movies = Movie.objects.filter(genre="판타지")[:15]
    serializer4 = MovieListSerializer(fantasy_movies, many=True)
    # 판타지 영화
    comedy_movies = Movie.objects.filter(genre="코미디")[:15]
    serializer5 = MovieListSerializer(comedy_movies, many=True)
    # 코미디 영화 
    romance_movies = Movie.objects.filter(genre="로맨스")[:15]
    serializer6 = MovieListSerializer(romance_movies, many=True)
    # 로맨스 영화
    sf_movies = Movie.objects.filter(genre="SF")[:15]
    serializer7 = MovieListSerializer(sf_movies, many=True)
    # SF 영화
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data, serializer5.data, serializer6.data, serializer7.data])


@api_view(['GET'])
def recommend(request):
# 개봉일순, 평점순, 랜덤 추천 영화 조회 (GET)
# 랜덤은 movie_list에서 함수 axios 요청하고 lodash로 vue에서 구현?
    high_movies = Movie.objects.all().order_by('-vote_average')[:30]
    serializer1 = MovieListSerializer(high_movies, many=True)
    # 평점 높은 영화
    low_movies = Movie.objects.all().order_by('vote_average')[:30]
    serializer2 = MovieListSerializer(low_movies, many=True)
    # 평점 낮은 영화
    recent_movies = Movie.objects.all().order_by('-release_date')[:30]
    serializer3 = MovieListSerializer(recent_movies, many=True)
    # 최신 영화
    old_movies = Movie.objects.all().order_by('release_date')[:30]
    serializer4 = MovieListSerializer(old_movies, many=True)
    # 오래된 영화
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data])

@api_view(['GET'])
def movie_list(request):
# 전체 영화 조회 (GET)
    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
# 상세 영화 조회 (GET)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk, user_pk):
# 상세 영화 좋아요(POST)
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 상세 영화
    if movie.like_user.filter(pk=user_pk).exists():
        movie.like_user.remove(request.user)
        liked = False
    else:
        movie.like_user.add(request.user)
        liked = True
    like_status = {
        'liked':liked,
        # 좋아요 여부
        'count':movie.like_user.count(),
        # 좋아요한 사람의 수
    }
    return Response(like_status, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
# 상세 영화 전체 리뷰 조회(GET) 리뷰 생성(POST)
  if request.method == 'GET':
  # 조회(GET)
    reviews = Review.objects.filter(movie_id=movie_pk)
    # 전체 리뷰 쿼리 조회 .all()
    # 외래키의 movie_id가 movie_pk와 일치하는 경우 .filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    # 복수 객체
    return Response(serializer.data)
  else:
  # 생성(POST)
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 상세 영화
    serializer = ReviewSerializer(data=request.data)
    # 단일 객체
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie = movie)
        # user, movie 외래키 참조 객체 설정
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
# 상세 영화 상세 리뷰 조회(GET), 수정(PUT), 삭제(DELETE)
    review = get_object_or_404(Review, pk=review_pk)
    # 상세 리뷰
    if request.method == 'GET':
    # 조회(GET)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    else:
        if request.user == review.user:
        # 리뷰 작성자와 같은 경우
            if request.method == 'DELETE':
            # 삭제(DELETE)
                review.delete()
                data = {
                    f'{review_pk}번 리뷰가 삭제되었습니다.'
                }
                return Response(data, status=status.HTTP_204_NO_CONTENT)
            if request.method == 'PUT':
            # 수정(PUT)
                serializer = ReviewSerializer(review, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
            # if not request.user.reviews.filter(pk=review_pk).exists():
            #     return Response({'message': '권한이 없습니다.'})
            # user : reviews 1:N 역참조 related name (reviews)

@api_view(['GET'])
def comment_list(request, review_pk):
# 상세 영화 상세 리뷰 전체 댓글 조회(GET)
    review = get_object_or_404(Review, pk=review_pk)
    # 상세 리뷰
    comments = review.comment_set.all()
    # 역참조 review : comment 1:N
    # 전체 댓글 .all()
    serializers = CommentSerializer(comments, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
# 상세 영화 상세 리뷰 댓글 생성(POST)
    review = get_object_or_404(Review, pk=review_pk)
    # 상세 리뷰
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review = review)
        # user, movie 외래키 참조 객체 설정
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, review_pk, comment_pk):
# 상세 영화 상세 리뷰 상세 댓글 삭제 (DELETE)
    # review = get_object_or_404(Review, pk=review_pk)
    # 상세 리뷰
    comment = get_object_or_404(Comment, pk=comment_pk)
    # 상세 댓글 .filter(pk=comment_pk)
    if request.user == comment.user:
    # 댓글 작성자와 같은 경우 
        comment.delete()
        data = {
            'delete': f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)
    # if not request.user.comments.filter(pk=comment_pk).exists():
    #     return Response({'message': '권한이 없습니다.'})
    # user : comments 1:N 역참조 related name (comments)

@api_view(['GET'])
def mbti(request):
# mbti 영화 유형별 조회 (GET)
    # mbtis = get_list_or_404(Mbti)
    # serializer = MbtiListSerializer(mbtis)
    estj_movies = Mbti.objects.filter(mbti="estj")
    serializer1 = MbtiListSerializer(estj_movies, many=True)
    istj_movies = Mbti.objects.filter(mbti="istj")
    serializer2 = MbtiListSerializer(istj_movies, many=True)
    estp_movies = Mbti.objects.filter(mbti="estp")
    serializer3 = MbtiListSerializer(estp_movies, many=True)
    istp_movies = Mbti.objects.filter(mbti="istp")
    serializer4 = MbtiListSerializer(istp_movies, many=True)
    infp_movies = Mbti.objects.filter(mbti="infp")
    serializer5 = MbtiListSerializer(infp_movies, many=True)
    enfp_movies = Mbti.objects.filter(mbti="enfp")
    serializer6 = MbtiListSerializer(enfp_movies, many=True)
    infj_movies = Mbti.objects.filter(mbti="infj")
    serializer7 = MbtiListSerializer(infj_movies, many=True)
    enfj_movies = Mbti.objects.filter(mbti="enfj")
    serializer8 = MbtiListSerializer(enfj_movies, many=True)
    esfp_movies = Mbti.objects.filter(mbti="esfp")
    serializer9 = MbtiListSerializer(esfp_movies, many=True)
    isfp_movies = Mbti.objects.filter(mbti="isfp")
    serializer10 = MbtiListSerializer(isfp_movies, many=True)
    entj_movies = Mbti.objects.filter(mbti="entj")
    serializer11 = MbtiListSerializer(entj_movies, many=True)
    intj_movies = Mbti.objects.filter(mbti="intj")
    serializer12 = MbtiListSerializer(intj_movies, many=True)
    isfj_movies = Mbti.objects.filter(mbti="isfj")
    serializer13 = MbtiListSerializer(isfj_movies, many=True)
    intp_movies = Mbti.objects.filter(mbti="intp")
    serializer14 = MbtiListSerializer(intp_movies, many=True)
    entp_movies = Mbti.objects.filter(mbti="entp")
    serializer15 = MbtiListSerializer(entp_movies, many=True)
    esfj_movies = Mbti.objects.filter(mbti="esfj")
    serializer16 = MbtiListSerializer(esfj_movies, many=True)
    return Response([serializer1.data, serializer2.data, serializer3.data, serializer4.data, serializer5.data, serializer6.data, serializer7.data, serializer8.data, serializer9.data, serializer10.data, serializer11.data, serializer12.data, serializer13.data, serializer14.data, serializer15.data, serializer16.data])

@api_view(['GET'])
def mbti_detail(request, mbti_movie_pk):
# mbti 상세 영화 조회 (GET)
    mbti = get_object_or_404(Mbti, pk=mbti_movie_pk)
    serializer = MbtiSerializer(mbti)
    return Response(serializer.data)

# mbti 상세 영화 리뷰
# mbti 영화 좋아요(POST)
# mbti 영화 전체 리뷰 조회(GET) 리뷰 생성(POST)
# models.py serialers.py views.py urls.py 새롭게 생성
# Mbti와 Movie는 model이 달라 movie의 mbti_movie_pk movie_pk가 다르기 때문에 별도로 작성 필요
# 리뷰 수정, 삭제, 상세 조회 및 댓글 작성, 조회, 삭제의 경우 review_pk만 필요해서 별도로 작성 불요
