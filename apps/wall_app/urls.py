from django.conf.urls import url
from . import views

#Wall_App#

urlpatterns = [
    url(r'^$', views.index),#wall/
    url(r'^post_message$', views.post_message), #wall/post_message
    url(r'^delete_message/(?P<id>\d+)$', views.delete_message), #wall/delete_message/id
    url(r'^add_comment/(?P<id>\d+)$', views.add_comment), #wall/add_comment/id
    url(r'^delete_comment/(?P<id>\d+)$', views.delete_comment), #wall/delete_comment/id
    url(r'^message/like/(?P<id>\d+)$', views.message_like), #wall/message/like/id
    url(r'^comment/like/(?P<id>\d+)$', views.comment_like), #wall/comment/like/id
]