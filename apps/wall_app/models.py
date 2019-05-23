from django.db import models
from datetime import datetime
from ..log_and_reg_app.models import *
import re


class Messages(models.Model):
    messager = models.ForeignKey(Users, related_name='users_messages')
    message_in_messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likes_on_message = models.ManyToManyField(Users, related_name="message_user_liked")

class Comments(models.Model):
    message_in_comments = models.ForeignKey(Messages, related_name='messages')
    commenter = models.ForeignKey(Users, related_name='users_comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    likes_on_comment = models.ManyToManyField(Users, related_name="comment_user_liked")
