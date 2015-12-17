from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
#from .models import *
#from .forms import *
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404

# Create your views here.

def home(request):

	return render_to_response('sitio/index.html',{},context_instance=RequestContext(request))