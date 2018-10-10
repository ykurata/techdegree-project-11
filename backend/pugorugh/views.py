from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
#from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class UserRegisterView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = get_user_model()
    serializer_class = serializers.UserSerializer


class RetrieveUpdateUserPref(generics.RetrieveUpdateAPIView):
    queryset = models.UserPref.objects.all()
    serializer_class = serializers.UserPrefSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            user=self.request.user)


class RetrieveDog(generics.RetrieveAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer

    def get_queryset(self):
        user = self.request.user
        user_pref = models.UserPref.objects.get(user=user)
        user_choice = self.kwargs.get('choice')

        age = user_pref.age
        size = user_pref.size
        gender = user_pref.gender

        matching_dogs = models.Dog.objects.all()

        if user_choice == 'undecided':
            matching_dogs = models.Dog.objects.filter(
                age__in=age,
                size__in=size,
                gender__in=gender,
                user_dog__status='u',
                user_dog__user=user
            ).order_by('pk')

        elif user_choice == 'disliked':
            matching_dogs = models.Dog.objects.filter(
                user_dog__status='d',
                user_dog__user=user
            ).order_by('pk')

        elif user_choice == 'liked':
            matching_dogs = models.Dog.objects.filter(
                user_dog__status='l',
                user_dog__user=user
            ).order_by('pk')

        return matching_dogs


    def get_object(self):
        pk = int(self.kwargs.get('pk'))
        dog = self.get_queryset().filter(id__gt=pk).first()
        if dog:
            return dog
        else:
            return self.get_queryset().first()


class UpdateDog(generics.UpdateAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer

    def get_queryset(self):
        pk = int(self.kwargs.get('pk'))

        dog = get_object_or_404(models.Dog, pk=pk)
        return dog

    def update(self, request, status, *args, **kwargs):
        status = self.kwargs.get('status')

        if status == 'liked':
            status = 'l'
        elif status == 'disliked':
            status = 'd'
        else:
            status = 'u'

        instance = self.get_object()
        #instance.status = request.data.get('status')
        #instance.save()

        serializer = self.get_serializer(
            instance,
            data={'status':status},
            partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serilalizer.data)
