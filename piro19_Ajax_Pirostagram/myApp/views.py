from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'myApp/main.html', {'posts' : posts, 'comments':comments})

@csrf_exempt
def like_ajax(request):
    reqObj = json.loads(request.body)
    post_id = reqObj['post_id']
    incdec = reqObj['incdec']

    post = Post.objects.get(id = post_id)

    if incdec == 'inc':
        post.like += 1
    else:
        if post.like > 0:
            post.like -= 1
    
    post.save()

    return JsonResponse({'post_id':post_id, 'like_cnt':post.like})

@csrf_exempt
def leave_comment_ajax(request):
    reqObj = json.loads(request.body)
    post_id = reqObj['post_id']
    comment = reqObj['comment']

    post = Post.objects.get(id = post_id)
    new_comment = Comment.objects.create(post = post, content = comment)

    return JsonResponse({'post_id':post_id, 'comment':comment, 'comment_id':new_comment.id})

@csrf_exempt
def remove_comment_ajax(request):
    reqObj = json.loads(request.body)
    comment_id = reqObj['comment_id']

    comment = Comment.objects.get(id = comment_id)
    comment.delete()

    return JsonResponse({'comment_id':comment_id})