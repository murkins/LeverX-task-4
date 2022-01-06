from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PersonaTestCase(APITestCase):
    personas_list_url = reverse('personas')

    def setUp(self):
        # create a new user by submitting a request to the djoser endpoint
        self.user = self.client.post('/auth/users/', data={'username': 'Mari', 'password': 'i-keep-jumping'})
        # get web token JSON for newly created user
        response = self.client.post('/auth/jwt/create/', data={'username': 'Mari', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # get a list of all user personas during user authentication request
    def test_personas_list_authenticated(self):
        response = self.client.get(self.personas_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # get a list of all user personas until the user's request is authenticated
    def test_personas_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.personas_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # check to get the persona details of the authenticated user
    def test_personas_detail_retrieve(self):
        response = self.client.get(reverse('persona', kwargs={'pk': 1}))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
