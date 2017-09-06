from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_app.urls', namespace='users')),
    url(r'^post/', include('apps.post_app.urls', namespace='posts')),
]
