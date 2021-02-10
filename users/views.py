from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .models import CustomUser
from .permissions import IsAdminOrMe
from .serializers import (
    ConfirmationCodeSerializer, CustomUserSerializer, UserEmailSerializer,
)
from api_yamdb.settings import EMAIL_HOST_USER


@api_view(['POST'])
def get_confirmation_code(request):
    username = request.data.get('username')
    serializer = UserEmailSerializer(data=request.data)
    email = request.data.get('email')
    serializer.is_valid(raise_exception=True)
    if username is not None:
        return Response(
            serializer.errors,
            status=status.HTTP_406_NOT_ACCEPTABLE
        )
    user = get_object_or_404(CustomUser, email=email)
    confirmation_code = default_token_generator.make_token(user)
    mail_subject = 'Код подтверждения'
    message = f'Ваш код подтверждения: {confirmation_code}'
    send_mail(
        mail_subject,
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_jwt_token(request):
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    confirmation_code = serializer.data.get('confirmation_code')
    user = get_object_or_404(CustomUser, email=email)
    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
    return Response(
        {'confirmation_code': 'Неверный код подтверждения'},
        status=status.HTTP_400_BAD_REQUEST
    )


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = (IsAdminOrMe,)

    @action(
        detail=False,
        methods=['get', 'patch'],
        url_path='me',
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        user = get_object_or_404(
            CustomUser,
            username=request.user.username
        )
        serializer = CustomUserSerializer(user)
        if request.method == 'PATCH':
            serializer = CustomUserSerializer(
                user,
                data=request.data,
                partial=True
            )
            if serializer.is_valid():
                serializer.save()
        return Response(serializer.data)
