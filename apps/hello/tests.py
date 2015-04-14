from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from models import RequestInfo, Contact


class ContactsPageTest(TestCase):

    def set_up(self):
        self.contact1 = Contact.objects.create(
            first_name="Albert",
            last_name="Lee",
            date_of_birth="1989-12-22",
            bio="bio",
            jabber="qwertty1232",
            email="albertlee@yandex.ru",
            skype="albertlee_1989",
            other_contacts="other"
        )
        self.contact2 = Contact.objects.create(
            first_name="Victor",
            last_name="Hertz",
            date_of_birth="1979-11-02",
            bio="biommm",
            jabber="crazy",
            email="vicher@gmail.com",
            skype="victor",
            other_contacts="other_contacts"
        )
        self.contact3 = Contact.objects.create(
            first_name="Vasya",
            last_name="Pupkin",
            date_of_birth="1990-12-22",
            bio="like biorobot",
            jabber="qwertty11",
            email="vasya@yandex.ru",
            skype="vasyaup",
            other_contacts="other_planete"
        )

    def test_home(self):
        """ method for testing main page"""
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '42 Coffee Cups Test Assingment')
        self.assertContains(response, 'Email: albertlee@yandex.ru')
        self.assertTemplateUsed(response, 'hello/home.html',)


class MiddlewareTest(TestCase):
    def test_middleware(self):
        """ method for testing middleware"""
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
