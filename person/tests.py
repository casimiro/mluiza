from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class FacebookUserTests(APITestCase):

    def test_create_facebook_user(self):
        """
        Test facebook creation
        """

        expectedData = {'username': 'gerald.thomas.967', 'facebookId': '1229015237', 'name': 'Gerald Thomas', 'gender': 'male'}

        response = self.client.post('/person/', {'facebookId': '1229015237'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expectedData)


    def test_delete_facebook_user(self):
        # registering user to be deleted
        self.client.post('/person/', {'facebookId': '1229015237'}, format='json')

        response = self.client.delete('/person/1229015237/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_list_facebook_user(self):
        self.client.post('/person/', {'facebookId': '1229015237'}, format='json')
        self.client.post('/person/', {'facebookId': '41'}, format='json')

        response = self.client.get('/person/?limit=0')
        self.assertEqual(len(response.data), 0)

        response = self.client.get('/person/?limit=1')
        self.assertEqual(len(response.data), 1)

        response = self.client.get('/person/?limit=2')
        self.assertEqual(len(response.data), 2)

        response = self.client.get('/person/')
        self.assertEqual(len(response.data), 2)
