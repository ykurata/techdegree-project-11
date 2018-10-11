from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
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

        age_group = []
        if 'b' in user_pref.age:
            for i in range(0, 10):
                age_group.append(i)
        if 'y' in user_pref.age:
            for i in range(10, 30):
                age_group.append(i)
        if 'a' in user_pref.age:
            for i in range(30, 70):
                age_group.append(i)
        if 's' in user_pref.age:
            for i in range(70, 999):
                age_group.append(i)

        matching_dogs = models.Dog.objects.filter(
            age__in=age_group,
            size__in=user_pref.size,
            gender__in=user_pref.gender
        )

        if user_choice == 'undecided':
            matching_dogs = matching_dogs.filter(
                userdog__status='u',
                userdog__user=user
            )

        elif user_choice == 'liked':
            matching_dogs = models.Dog.objects.filter(
                userdog__status='l',
                userdog__user=user
            )

        elif user_choice == 'disliked':
            matching_dogs = models.Dog.objects.filter(
                userdog__status='d',
                userdog__user=user
            )

        return matching_dogs


    def get_object(self):
        pk = self.kwargs.get('pk')
        dog = self.get_queryset().filter(id__gt=pk).first()
        if not dog:
            raise Http404
        else:
            return dog


class UpdateDog(generics.UpdateAPIView):
    queryset = models.Dog.objects.all()
    serializer_class = serializers.DogSerializer

    def get_queryset(self):
        pk = int(self.kwargs.get('pk'))

        dog = get_object_or_404(models.Dog, pk=pk)
        return dog

    def update(self, request, *args, **kwargs):
        user_choice = self.kwargs.get('choice')

        if user_choice == 'liked':
            choice = 'l'
        elif user_choice == 'disliked':
            choice = 'd'
        else:
            choice = 'u'

        instance = self.get_object()
        #instance.status = request.data.get('status')
        #instance.save()

        serializer = self.get_serializer(
            instance,
            data={'user_choice':choice},
            partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serilalizer.data)
