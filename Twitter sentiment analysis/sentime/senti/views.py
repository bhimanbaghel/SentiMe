from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import People
from scripts import sample

def search(request):
	if request.method == 'GET':
		return render(request, 'senti/search.html')
	else:
		search = request.POST.get('search')
		acc = sample.main(search)
		context = {
			'search': search,
			'acc': acc,
		}
		return render(request, 'senti/search.html', context)
		
def index(request):
	if request.method == 'GET':
		return render(request, 'senti/index.html')
	else:
		search = request.POST.get('search')
		acc = sample.main(search)
		context = {
			'search': search,
			'acc': acc,
		}
		return render(request, 'senti/index.html', context)