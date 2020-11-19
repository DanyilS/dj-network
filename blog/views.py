from django.shortcuts import render

from .models import Post


def profile(request):

    posts = Post.objects.filter(owner=request.user)

    context = {
        'user_posts': posts
    }

    return render(request, 'profile_detail.html', context=context)

