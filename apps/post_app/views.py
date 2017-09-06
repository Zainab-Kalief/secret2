from django.shortcuts import render, redirect
from ..user_app.models import User
from django.contrib import messages
from .models import Secret, Like

# Create your views here.
def home(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {'user': user, 'secrets': Secret.objects.all().order_by('-created_at'), 'user_likes': Like.objects.filter(user_id=user.id)
                    }
    return render(request, 'post_app/home.html', context)

def post_secret(request):
    user = User.objects.get(id=request.session['user_id'])
    entry = Secret.objects.create_secret(request.POST, user)
    if entry == False:
        messages.add_message(request, messages.INFO, 'Type your secret here', extra_tags='no_secret')
    return redirect('posts:home')


def add_like(request, secret_id):
    user = User.objects.get(id=request.session['user_id'])
    secret = Secret.objects.get(id=secret_id)
    entry = Like.objects.create_like(secret, user)
    return redirect('posts:home')

def delete_secret(request, secret_id):
    secret = Secret.objects.get(id=secret_id)
    secret.delete()
    return redirect('posts:home')

def most_likes(request):
    context = {'secrets': Secret.objects.all().order_by('-secret_likes')}
    return render(request, 'post_app/popular.html', context)
