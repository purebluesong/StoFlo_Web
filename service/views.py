from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
import django.conf.urls
import files
from str_ import *
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
	return render_to_response(files.index, content)

@csrf_exempt
def login(request):
	if username_str in request.POST and password_str in request.POST and request.POST[username_str] and request.POST[password_str]:
		username = request.POST[username_str]
		password = request.POST[password_str]
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			soureceurl = request.POST.get('soureceurl')
			return HttpResponseRedirect('/') if not soureceurl else HttpResponseRedirect(soureceurl)
		else:
			request.session['errors'] = ['invalid password or username, please try again']
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

@csrf_exempt
def login_cln(request):
	if username_str in request.POST and password_str in request.POST and request.POST[username_str] and request.POST[password_str]:
		username = request.POST[username_str]
		password = request.POST[password_str]
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return {'suceess':True}
	return {'seceess':False}

@csrf_exempt
def regeister(request):
	return none

@csrf_exempt
def show_test(request):
	return render_to_response(files.test,{})
