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