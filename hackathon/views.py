from django.shortcuts import render
from .models import Hackathon, HackathonParticipant
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet, ModelViewSet
from .serializers import HackathonSerializer, UserSerializer,HackathonParticipantSerializer
from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Create your views here.
class HackathonViewSet(ModelViewSet):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })


class HackathonParticipantViewSet(ModelViewSet):
    queryset = HackathonParticipant.objects.all()
    serializer_class = HackathonParticipantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# class SubmissionEditPermission(BasePermission):
    
#         message = 'You are not the owner of this submission.'
    
#         def has_object_permission(self, request, view, obj):
#             if request.method in SAFE_METHODS:
#                 return True
#             return obj.user == request.user


# class SubmissionViewSet(ModelViewSet, SubmissionEditPermission):
#     queryset = Submission
#     serializer_class = SubmissionSerializer
#     permission_classes = [SubmissionEditPermission]

class UserAtleastOne(APIView):
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        users = User.objects.filter(participating_hackathons__isnull=False).distinct()
        serilizer = UserSerializer(users, many=True)
        return Response(serilizer.data)
    
class UserNotAtleastOne(APIView):
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        users = User.objects.filter(participating_hackathons__isnull=True).distinct()
        serilizer = UserSerializer(users, many=True)
        return Response(serilizer.data)