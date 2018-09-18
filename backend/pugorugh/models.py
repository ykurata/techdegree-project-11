from django.contrib.auth.models import User
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
    image_filename = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

    def __str__(self):
        return self.name


class UserDog(models.Model):
    LIKED = "l"
    DISLIKED = "d"
    STATUS_CHOICES = (
        (LIKED, "Liked"),
        (DISLIKED, "Disliked")
    )
    user = models.ForeignKey(User)
    dog = models.ForeignKey(Dog)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


class UserPref(models.Model):
    BABY = "b"
    YOUNG = "y"
    ADULT = "a"
    SENIOR = "s"
    AGE_CHOICES = (
        (BABY, "Baby"),
        (YOUNG, "Young"),
        (ADULT, "Adult"),
        (SENIOR, "Senior")
    )

    MALE = "m"
    FEMALE = "f"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )

    SMALL = "s"
    MEDIUM = "m"
    LARGE = "l"
    EXTRA_LARGE = "xl"
    SIZE_CHOICES = (
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
        (EXTRA_LARGE, "Extra large")
    )
    user = models.ForeignKey(User)
    age = models.CharField(max_length=1, choices=AGE_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
