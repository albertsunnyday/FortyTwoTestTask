
from annoying.decorators import render_to
from apps.hello.models import Contact, RequestInfo
from django.contrib.auth.models import User


@render_to('hello/home.html')
def home(request):
    contact = Contact.objects.get(pk=1)
    return {'contact': contact}


@render_to('hello/requests.html')
def requests(request):
    requestinfo = RequestInfo.objects.all()[:10]
    return {'requests': requestinfo}


def fixtures(request):
    contact = Contact()
    contact.email = 'albertlee@yandex.ru'
    contact.first_name = 'albert'
    contact.last_name = 'lee'
    contact.jabber = 'jabber_id'
    contact.date_of_birth = '2015-04-02'
    contact.save()
    user = User.objects.create_user('admin', 'admin@thebeatles.com', 'admin')
    user.is_superuser = True
    user.is_staff = True
    user.save()
