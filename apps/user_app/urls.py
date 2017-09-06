from django.conf.urls import url
from . import views
app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='register'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^register_test$', views.register_test, name='register_test'),
    url(r'^log_in_test$', views.log_in_test, name='log_in_test'),

]
