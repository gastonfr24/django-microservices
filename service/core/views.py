from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class DecodeTokenView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        user = request.user
        data = {
            "id":user.id,
            "username":user.username,
            "roles":user.roles
        }
        return Response({"user_data": data})