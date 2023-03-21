from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
	print("Tests: ")
	print("===========================")
	print("Get restaurants data")
	print("Get restaurant detail data")
	print("===========================")
	
	def setUp(self):
		return super().setUp()

	def tearDown(self):
		return super().tearDown()
