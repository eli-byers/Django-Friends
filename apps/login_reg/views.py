from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User
root = 'login_reg:root'

def index(request):
	return render(request, 'login_reg/index.html')

def login(request):
	route = root
	if request.method == "POST":
		result = User.objects.login(request.POST)
		route = processLogin(request, result)
	return redirect(reverse(route))

def register(request):
	route = root
	if request.method == "POST":
		result = User.objects.registerUser(request.POST)
		route = processLogin(request, result)
	return redirect(reverse(route))

def processLogin(request, result):
	if result['status']:
		request.session['user_id'] = result['user_id']
		route = 'friends:home'
	else:
		for error in result['errors']:
			messages.error(request, error['message'], extra_tags = error['tag'])
		route = root
	return route

def logout(request):
	request.session.clear()
	return redirect(reverse(root))
