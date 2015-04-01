
from annoying.decorators import render_to
from apps.hello.models import Contact


@render_to('hello/home.html')
def home(request):
	contact = Contact.objects.get(pk=1)
	return {'contact': contact}
