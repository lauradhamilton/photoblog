from django.conf.urls import url

from post.views import index, Post

urlpatterns = [
  url(r'^$', index),
]
