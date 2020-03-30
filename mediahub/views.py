import random
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from moviepy import editor

from .forms import PostForm
from .models import *


@login_required(redirect_field_name='accounts/login')
def index(request):
    posts = Post.objects.all()
    context = getContext(posts)
    context['posts'] = posts
    context['categories'] = Category.objects.all()
    context['contentHeader'] = "Dashboard"
    context['contentBreadcrumb'] = "Home"

    return render(request, 'mediahub/index.html', context)


def search(request):
    category = request.GET.get('category')
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')

    if category:
        post_list = Post.objects.filter(category=category).order_by('createdOn')
    else:
        post_list = Post.objects.all()

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
        post_list = Post.objects.filter(createdOn__range=[start_date, end_date])

    return render(request, 'mediahub/post/post_list.html', {'posts': post_list})


def add_post(request):
    posts = Post.objects.all()
    context = getContext(posts)
    context['contentHeader'] = "Add new post"
    context['contentBreadcrumb'] = "Home"

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.createdBy = User
            form.save()
            form = PostForm()
            context['form'] = form

            context['successMessage'] = 'Your Post was successfully uploaded.'
            return render(request, 'mediahub/index.html', context)

    else:
        form = PostForm()

    context['form'] = form

    return render(request, 'mediahub/post/add_post.html', context)


def generate_thumbnails(post_id):
    post = Post.objects.get(pk=post_id)
    clip = editor.VideoFileClip(post.filename())
    thumbnail = os.path.join("media/thumbs/", "thumbnail_%s.png" % post.id)
    clip.save_frame(thumbnail, t=random.uniform(0.1, clip.duration))
    return thumbnail


def getContext(posts):
    sidebarMenu = Category.objects.all()
    context = {'sidebarMenu': sidebarMenu}
    if posts:
        context['posts'] = posts

    return context
