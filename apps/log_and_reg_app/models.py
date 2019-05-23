from django.db import models
from datetime import datetime
import re

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        current_time = datetime.now()
        grab = Users.objects.filter(email = postData['email'])

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email1'] = "Invalid email address"
        if len(grab) > 0:
            errors['email2'] = "Email already exists"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords should match"
        if postData['birthday'] > str(current_time):
            errors['birthday1'] = "Birthday cannot be in the future"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        grab = Users.objects.filter(email = postData['email'])

        if not EMAIL_REGEX.match(postData['email']):
            errors['email1'] = "Invalid email address"
        if len(grab) == 0:
            errors['email2'] = "Please register email"
        else:
            user = Users.objects.get(email = postData['email'])
            if postData['password'] != user.password:
                errors['password2'] = "Incorrect password"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    birthday = models.DateTimeField()
    email = models.CharField(max_length = 45)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UsersManager()