from django.urls import path
# path
from . import views
# views

app_name = 'movies'
# 앱 네임 설정
urlpatterns = [
    path('genre/', views.genre, name='genre'),
    # 장르별 추천 영화 조회 (GET)
    path('recommend/', views.recommend, name='recommend'),
    # 개봉일순, 평점순, 랜덤 추천 영화 조회 (GET)
    
    path('mbti/', views.mbti, name='mbti'),
    path('mbti/<int:mbti_movie_pk>/', views.mbti_detail, name='mbti_detail'),
    # mbti 추천

    path('', views.movie_list, name='movie_list'),
    # 전체 영화 조회(GET)
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # 상세 영화 조회(GET)
    path('<int:user_pk>/<int:movie_pk>/like/', views.movie_like, name='movie_like'),
    # 상세 영화 좋아요(POST)
    # 프로필로 axios 요청해서user 정보 담고 user.id로 접근하기

    path('<int:movie_pk>/review/', views.review_list_create, name='review_list_create'),
    # 상세 영화 전체 리뷰 조회(GET) 리뷰 생성(POST)
    
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),
    # 상세 영화 상세 리뷰 조회(GET), 수정(PUT), 삭제(DELETE)

    path('review/<int:review_pk>/comments/', views.comment_list, name='comment_list'),
    # 상세 영화 상세 리뷰 전체 댓글 조회(GET)
    path('review/<int:review_pk>/comment/', views.comment_create, name='comment_create'),
    # 상세 영화 상세 리뷰 댓글 생성(POST)
    path('review/<int:review_pk>/comment/<int:comment_pk>/', views.comment_delete, name = 'comment_delete'),
    # 상세 영화 상세 리뷰 상세 댓글 삭제 (DELETE)

    path('<int:user_pk>/likes/', views.user_likes, name='user_likes'),
    # 사용자가 좋아요한 영화 (GET)
    path('<int:user_pk>/reviews/', views.user_reviews, name='user_reviews'),
    # 사용자가 생성한 리뷰 조회 (GET)
    path('<int:user_pk>/comments/', views.user_comments, name='user_comments'),
    # 사용자가 생성한 댓글 조회 (GET)
]
