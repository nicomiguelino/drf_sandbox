from rest_framework.views import APIView
from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        content = {
            'message': 'Hello, World!',
            'user': {
                'username': request.user.username,
                'email': request.user.email,
                'is_active': request.user.is_active,
                'is_staff': request.user.is_staff
            }
        }
        return Response(content)