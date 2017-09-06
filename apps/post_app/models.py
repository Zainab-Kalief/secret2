from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

# Create your models here.
class SecretManager(models.Manager):
    def create_secret(self, data, user):
        if not data['secret']:
            return False
        else:
            return self.create(secret=data['secret'], user=user)

class LikeManager(models.Manager):
    def create_like(self, secret, user):
        if self.filter(secret=secret, user=user):
            return False
        else:
            return self.create(secret=secret, user=user)

class Secret(models.Model):
    secret = models.TextField(max_length=2000)
    user = models.ForeignKey(User, related_name='secrets')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = SecretManager()
    def secret_user_likes(self):
        likes = Like.objects.filter(secret=self)
        users = []
        for user in likes:
            users.append(user.user)
        return users


class Like(models.Model):
    secret = models.ForeignKey(Secret, related_name='secret_likes')
    user = models.ForeignKey(User, related_name='user_likes')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = LikeManager()
