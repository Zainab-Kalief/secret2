from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')

def log_in(request):
    return render(request, 'user_app/log_in.html')

def register_test(request):
    entry = User.objects.create_user(request.POST)
    if not type(entry) is dict:
        request.session['user_id'] = entry.id
        return redirect('posts:home')
    else:
        if 'name' in entry:
            messages.add_message(request, messages.INFO, entry['name'], extra_tags='sign_up')
        if 'email' in entry:
            messages.add_message(request, messages.INFO, entry['email'], extra_tags='sign_up')
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'], extra_tags='sign_up')
        if 'confirm_password' in entry:
            messages.add_message(request, messages.INFO, entry['confirm_password'], extra_tags='sign_up')
        if 'email_exist' in entry:
            messages.add_message(request, messages.INFO, entry['email_exist'], extra_tags='sign_up')
        return redirect('users:register')

def log_in_test(request):
    entry = User.objects.validate_user(request.POST)
    if not type(entry) is dict:
        request.session['user_id'] = entry.id
        return redirect('posts:home')
    else:
        if 'email' in entry:
            messages.add_message(request, messages.INFO, entry['email'], extra_tags='log_in')
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'], extra_tags='log_in')
        return redirect('users:log_in')    
