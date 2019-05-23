from django.shortcuts import render, HttpResponse, redirect
from ..log_and_reg_app.models import Users
from .models import Messages, Comments

#Wall_App#

def index(request):
    context = {
        "logged_in": Users.objects.get(id = request.session['user_id']),
        "messages_posted": Messages.objects.order_by('-created_at'),
        "comments_posted": Comments.objects.order_by('created_at'),
    }
    return render(request, 'wall_app/index.html', context)

def post_message(request):
    if request.method == "POST":
        user = Users.objects.get(id = request.session['user_id'])
        new_message = Messages.objects.create(messager = user, message_in_messages = request.POST['message'])
    return redirect("/wall")

def delete_message(request, id):
    dead_post = Messages.objects.get(id = id)
    dead_post.delete()
    return redirect("/wall")

def add_comment(request, id):
    focus_of_comment = Messages.objects.get(id = id)
    user = Users.objects.get(id = request.session['user_id'])
    new_comment = Comments.objects.create(message_in_comments = focus_of_comment, commenter = user, comment = request.POST['comment'])
    return redirect("/wall")

def delete_comment(request, id):
    dead_comment = Comments.objects.get(id = id)
    dead_comment.delete()
    return redirect("/wall")

def message_like(request, id):
    user_that_is_liking = Users.objects.get(id = request.session['user_id'])
    message_to_like = Messages.objects.get(id = id)
    message_to_like.likes_on_message.add(user_that_is_liking)
    message_to_like.save()
    return redirect("/wall")

def comment_like(request, id):
    user_that_is_liking = Users.objects.get(id = request.session['user_id'])
    comment_to_like = Comments.objects.get(id = id)
    comment_to_like.likes_on_comment.add(user_that_is_liking)
    comment_to_like.save()
    return redirect("/wall")