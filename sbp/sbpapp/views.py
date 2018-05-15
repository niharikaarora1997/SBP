# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User_Info

@csrf_exempt
def post(request):
	User_Info.objects.create(username=request.POST["username"],email=request.POST["email"],address=request.POST["address"])
	return JsonResponse({"message":"registered"})
	
def get_username(request):
	pattern=request.GET["pattern"]
	query=User_Info.objects.filter(username__contains=pattern)
	data=[]
	for a in query:
		data.append({a.username:"result"})
	return JsonResponse(data,safe=False)	

def get_email(request):
	pattern=request.GET["pattern"]
	print "ema"
	query=User_Info.objects.filter(email__contains=pattern)
	data=[]
	for a in query:
		data.append({a.email:"result"})
	return JsonResponse(data,safe=False)	

def get_address(request):
	pattern=request.GET["pattern"]
	query=User_Info.objects.filter(address__contains=pattern)
	data=[]
	for a in query:
		data.append({a.address:"result"})
	return JsonResponse(data,safe=False)	
	
