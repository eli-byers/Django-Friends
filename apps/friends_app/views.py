from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..login_reg.models import User

def home(request):
	if 'user_id' in request.session:
		user = User.objects.get(id = request.session['user_id'])
		user_ids = list(user.friends.values_list('id', flat=True))
		user_ids.append(request.session['user_id'])
		other_users = User.objects.exclude(id__in=user_ids)
		context = {
			'user': user,
			'other_users': other_users
		}
		return render(request, 'friends_app/index.html', context)
	return redirect(reverse('login_reg:root'))

def add_friend(request, id):
	if 'user_id' in request.session:
		friend = User.objects.filter(id=id)
		if friend:
			user = User.objects.get(id=request.session['user_id'])
			user.friends.add(friend[0])
		return redirect(reverse('friends:home'))
	return redirect(reverse('login_reg:root'))

def remove_friend(request, id):
	if 'user_id' in request.session:
		friend = User.objects.filter(id=id)
		if friend:
			user = User.objects.get(id=request.session['user_id'])
			user.friends.remove(friend[0])
		return redirect(reverse('friends:home'))
	return redirect(reverse('login_reg:root'))

def view_profile(request, id):
	user = User.objects.filter(id=id)
	if user:
		context = { "user": user[0] }
		return render(request, 'friends_app/show.html', context)
	return redirect(reverse('friends:home'))
