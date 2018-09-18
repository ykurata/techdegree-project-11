from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
#from rest_framework.views import APIView
#from rest_framework.response import Response

from . import models
from . import serializers


class UserRegisterView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = serializers.UserSerializer


class ListCreateDog(generics.ListCreateAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer


class RetrieveUpdateDestroyDog(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer


class ListCreateUserPref(generics.ListCreateAPIView):
    queryset = models.UserPref.objects.all()
    serializer_class = serializers.UserPrefSerializer


class RetrieveUpdateDestroyUserPref(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserPref.objects.all()
    serializer_class = serializers.UserPrefSerializer

""""
class ListCreateDog(APIView):
    def get(self, request, format=None):
        dogs = models.Dog.objects.all()
        serializer = serializers.DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.DogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""
