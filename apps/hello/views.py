
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

