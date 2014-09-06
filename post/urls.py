from django.conf.urls import url

from post.views import index

urlpatterns = [
  url(r'^$', index),
]
