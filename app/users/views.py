from django.contrib.auth import authenticate

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request:Request)->Response:
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username,password=password)
        
        if not user:
            return Response({"detail":"Munday username foydalanuvchisi  yuq"},status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = RefreshToken.for_user(user)
        
        response = Response({
            "Access": str(refresh.access_token)
        })
        
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=60 * 60 * 24 * 30
        )
        return response
    
    
class RefreshView(APIView):
    permission_classes = [AllowAny]
    
    def post(self,request:Request)->Response:
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            return Response({
                "detail":"Refresh token muddati  tugagan"
            },status=status.HTTP_401_UNAUTHORIZED)
            
        try:
            refresh = RefreshToken(refresh_token)
            return Response({
                "Access": str(refresh.access_token)
            })
        except Exception:
            return Response({
                "detail": "Invalid refresh token"
            },status=status.HTTP_401_UNAUTHORIZED)
            
        
        
class LogoutView(APIView):
    def post(self,request:Request)->Response:
        response = Response({"detail":"Siz Logout Bo'ldingz"})
        response.delete_cookie("refresh_token")
        return response




class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not user.check_password(old_password):
            return Response(
                {"detail": "Passwordni tug'ri kiriting"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password O'zgartirildi"})
