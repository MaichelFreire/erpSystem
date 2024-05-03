from .base import Base
from ..models import User
from ..serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GetUser(Base):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        print(user, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        enterprise = self.get_enterprise_user(user)

        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise
        })