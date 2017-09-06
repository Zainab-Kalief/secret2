from django.conf.urls import url
from . import views
app_name = 'posts'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^home/post_secret$', views.post_secret, name='post_secret'),
    url(r'^home/add_like/(?P<secret_id>\d+)$', views.add_like, name='add_like'),
    url(r'^home/delete_secret/(?P<secret_id>\d+)$', views.delete_secret, name='delete_secret'),
    url(r'^home/most_likes$', views.most_likes, name='most_likes'),
]
