import logging
from annoying.decorators import render_to
from apps.hello.models import Contact, RequestInfo
from django.contrib.auth.models import User

logger_info = logging.getLogger('contact.info')
logger_debug = logging.getLogger('contact.debug')


@render_to('hello/home.html')
def home(request):
    logger_info.info('User requested path: %s', request.path)
    contact = Contact.objects.get(pk=1)
    logger_debug.debug('Data sent: %s', contact)
    return {'contact': contact}


@render_to('hello/requests.html')
def requests(request):
    logger_info.info('User requested path: %s', request.path)
    requestinfo = RequestInfo.objects.all()[:10]
    logger_debug.debug('Data sent: %s', requestinfo)
    return {'requests': requestinfo}


def fixtures(request):
    contact = Contact()
    contact.first_name = 'Albert'
    contact.last_name = 'Lee'
    contact.date_of_birth = '1989-12-22'
    contact.bio = 'some bio'
    contact.email = 'albertlee@yandex.ru'
    contact.jabber = 'jabber_id'
    contact.skype = 'albertlee_1989'
    contact.other_contacts = 'other'
    contact.save()
    user = User.objects.create_user('admin', 'admin@thebeatles.com', 'admin')
    user.is_superuser = True
    user.is_staff = True
    user.save()

