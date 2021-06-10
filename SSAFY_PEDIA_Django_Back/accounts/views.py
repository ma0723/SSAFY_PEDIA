from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# DRF

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# TOKEN 유효여부와 인증을 위한 데코레이터 (JWT)

from django.contrib.auth import get_user_model
# models.py 제외하고 get_user_model()
from .serializers import UserSerializer

@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    # Client에서 온 데이터를 받기
    if password != password_confirmation:
    # 패스워드 일치 여부 체크
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)
    # UserSerializer를 통해 데이터 직렬화
    if serializer.is_valid(raise_exception=True):
    # 유효성 검사(비밀번호도 직렬화)
        user = serializer.save()
        user.set_password(request.data.get('password'))
        # 비밀번호 해싱
        user.save()
        # password는 직렬화되어도 response에서 표현되지 않는다
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 로그아웃
# 탈퇴
# 회원정보 수정
# 비밀번호 변경

@api_view(['POST'])
def profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    # 사용자 본인 jwt의 user_id (url에 정보가 없다)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def profile_search(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    # 타인의 user_pk (url에 username 정보가 있다)
    # ReviewDetail에서 작성자의 username을 클릭하면 그 사람 프로필로 이동
    # params 인자로 user의 정보를 넘겨서 user_pk로 검색
    serializer = UserSerializer(user)
    return Response(serializer.data)

# @api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def follow(request, my_pk, your_pk):
#     you = get_object_or_404(get_user_model(), pk=your_pk)
#     me = get_object_or_404(get_user_model(), pk=my_pk)
#     if you != me:
#         if me.followings.filter(pk=you.pk).exists():
#             me.followings.remove(you)
#             followed = False
#         else:
#             me.followings.add(you)
#             followed = True
#     followed_status = {
#         'followed':followed,
#         # 팔로우 여부
#         'followings': you.followings.count(),
#         # 팔로잉 수
#         'followers': you.followers.count(),
#         # 팔로워 수
#         # 팔로잉 목록과 팔로워 목록 추가?
#     }
#     return Response(followed_status, status=status.HTTP_200_OK)