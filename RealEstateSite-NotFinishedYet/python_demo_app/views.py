from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def python_demo_app (request):
	template = loader.get_template('myfirst.html')
	#return HttpResponse ("<H2> Python Artificial Intelligence Demo </H2>")
	return HttpResponse (template.render())

# Create your views here.
