from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

class HttpTest(TestCase):
	def test_home(self):
		c = Client()
		response = c.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '42 Coffee Cups Test Assingment')
		self.assertContains(response, 'Email: albertlee@yandex.ru')
		self.assertTemplateUsed(response, 'hello/home.html',)

	def test_middleware(self):
		self.client.get(reverse('home'))
		self.client.get(reverse('requests'))
		req_count = RequestInfo.objects.all().count()
		req = RequestInfo.objects.get(pk=1)
		self.assertEqual(req_count, 1)
		self.assertEqual(req.path, reverse('home'))
		self.assertEqual(req.method, 'GET')
		response = self.client.get(reverse('requests'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '42 Coffee Cups Test Assingment')
		self.assertContains(response, reverse('home'))
		self.assertTemplateUsed(response, 'hello/requests.html',)