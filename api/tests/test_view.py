from .test_setup import TestSetUp
from django.urls import reverse
from rest_framework import status

class TestViews(TestSetUp):

	def test_get_restuarants_api(self):
		location = 'California'
		search_term = 'Sushi'
		# constructing url 
		url = reverse('restaurants')
		url += f'?location={location}&search_term={search_term}'
		# make a GET request to the url

		response = self.client.get(url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_restuarants_detail_api(self):
		url = reverse('restaurants-detail', kwargs={'pk': '2CPJ0visHY4zAgHIw0HvNA'})
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

