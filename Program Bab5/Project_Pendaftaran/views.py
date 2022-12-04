from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')
def about(request):
	return render(request, 'about.html')
def index2(req):
	return HttpResponse("<h1>Halo Web Pendaftaran (index2)</h1>")
