import logging
from annoying.decorators import render_to
from apps.hello.models import Contact, RequestInfo


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
