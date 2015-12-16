from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
import django.conf.urls
from service import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# from django.utils.timezone import now
# import datetime
# import json
# import sys
# import xlwt
# import StringIO

# Create your views here.

def getIndexInfo():
	return {}

@csrf_exempt
def index(returnequest):
	content = getIndexInfo()
	return render_to_response('index.html', content)

def login(request):
	return none

def regeister(request):
	return none
