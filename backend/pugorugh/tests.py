from django.test import TestCase

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
#from rest_framework.test import force_authenticate
from .models import Dog, UserDog, UserPref
from . import views


class CreateUserTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(
            username='yasuko',
            password='password'
        )

    def test_register_user(self):
        url = reverse('register-user')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestUserPref(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_userpref(self):
        userpref = UserPref.objects.create(
            user=self.user,
            age='b',
            gender='f',
            size='s'
        )
        url = reverse('user_pref')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)


class TestRetrieveDog(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


        self.userpref = UserPref.objects.create(
            user=self.user,
            age='b,y,a,s',
            gender='m,f',
            size='s,m,l,xl'
        )

        self.dog = Dog.objects.create(
            name='test dog',
            image_filename='dog.pics',
            breed='husky',
            gender='f',
            size='m',
            age='10'
        )

        self.userdog = UserDog.objects.create(
            user=self.user,
            dog=self.dog,
            status='u'
        )

    def test_get_undecided_dog(self):
        response = self.client.get('/api/dog/-1/undecided/next/', format='json')
        self.assertEqual(response.status_code, 200)


class TestUpdateDog(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.userpref = UserPref.objects.create(
            user=self.user,
            age='b,y,a,s',
            gender='m,f',
            size='s,m,l,xl'
        )

        self.dog = Dog.objects.create(
            name='test dog',
            image_filename='dog.pics',
            breed='husky',
            gender='f',
            size='m',
            age='10'
        )

        self.userdog = UserDog.objects.create(
            user=self.user,
            dog=self.dog,
            status='l'
        )

    def test_update_dog_status(self):
        response = self.client.put('/api/dog/1/liked/', format='json')
        self.assertEqual(response.status_code, 200)
