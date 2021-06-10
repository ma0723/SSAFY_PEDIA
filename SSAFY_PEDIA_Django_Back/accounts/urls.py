from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'
urlpatterns = [
    path('api-token-auth/', obtain_jwt_token),
    # 로그인
    path('signup/', views.signup, name='signup'),
    # 회원가입
    path('profile/', views.profile, name='profile'),
    # 나의 프로필
    path('<int:user_pk>/profile/', views.profile_search, name='profile_search'),
    # 타인 프로필
    # path('follow/<int:my_pk>/<int:your_pk>/', views.follow, name='follow'),
    # 팔로우 
]
