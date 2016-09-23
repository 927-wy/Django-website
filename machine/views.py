import datetime
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponse

from django.template import loader

def index(request):
    
    now=datetime.datetime.now()
    return render_to_response('machine/index.html', {'now':now})

