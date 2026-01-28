from rest_framework.response import Response #type:ignore
from rest_framework.views import APIView #type:ignore
from rest_framework import status #type:ignore
from rest_framework.authtoken.models import Token #type:ignore
from django.contrib.auth import authenticate

class APILoginView(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")

        user=authenticate(username=username,password=password)
        if user:
            token, created=Token.objects.get_or_create(user=user)
            return Response(
                {
                  "token" :token.key,
                  "username": user.username,
                  "message": "Login successful ✅"
                  
                }
            )
        return Response({"error": "Invalid credentials ❌"}, status=status.HTTP_401_UNAUTHORIZED)