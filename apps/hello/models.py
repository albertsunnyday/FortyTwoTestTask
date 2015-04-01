from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField()
    bio = models.TextField(blank=True)
    jabber = models.CharField(max_length=50, blank=True)
    skype = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    other_contacts = models.TextField(blank=True)

    def __unicode__(self):
        return self.email


class RequestInfo(models.Model):
    method = models.CharField(max_length=5)
    path = models.CharField(max_length=70)
    time = models.DateTimeField(auto_now_add=True)
