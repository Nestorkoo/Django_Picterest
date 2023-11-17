from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def main(request):
    pictures = Create_Post.objects.all()

    return render(request, 'mainapp/index.html', {'pictures': pictures})


def picture_detail(request, photo_id):
    picture = get_object_or_404(Create_Post, pk=photo_id)
    related_posts = picture.get_related_posts()

    context = {
        'picture': picture,
        'related_posts': related_posts,
    }
    return render(request, 'mainapp/pictures_detail.html', context=context)


def add_post(request):
    form = AddCardImage()
    error = ''
    if request.method == 'POST':
        form = AddCardImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Something went wrong :('
    else:
        form = AddCardImage()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/add_post.html', context=context)

