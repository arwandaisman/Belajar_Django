from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> Hello, Web My Name</h1>")
