from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models


class Dog(models.Model):
    MALE = "m"
    FEMALE = "f"
    UNKNOWN = "u"
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNKNOWN, 'Unknown')
    )

    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"
    EXTRA_LARGE = "xl"
    UNKNOWN = "u"
    SIZE_CHOICES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
        (EXTRA_LARGE, "Extra large"),
        (UNKNOWN, "u")
    )
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255, blank=True)
    breed = models.CharField(max_length=255, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    age_group = models.CharField(max_length=10, default="b")

    def __str__(self):
        return self.name


class UserDog(models.Model):
    LIKED = "l"
    DISLIKED = "d"
    UNKNOWN = "u"
    STATUS_CHOICES = (
        (LIKED, "Liked"),
        (DISLIKED, "Disliked"),
        (UNKNOWN, "Unkown")
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    dog = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES)


    def __str__(self):
        return '{} and {}'.format(str(self.user), str(self.dog))


class UserPref(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_pref")
    age = models.CharField(
        max_length=10,
        default='b,y,a,s')
    gender = models.CharField(
        max_length=10,
        default='m,f')
    size = models.CharField(
        max_length=10,
        default='s,m,l,xl')

    def __str__(self):
        return '{}'.format(str(self.user))
