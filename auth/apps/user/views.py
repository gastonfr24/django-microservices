import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DecodeTokenView(APIView):
    def post(self, request):
        token = request.data.get('token', None)
        if not token:
            return Response({"error": "Token not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_token = jwt.decode(token, options={"verify_signature": False})
            return Response(decoded_token, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
