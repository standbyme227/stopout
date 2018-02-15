from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def webtoon_list(request):

    webtoons = Webtoon.objects.all()
    context = {
        'webtoons':webtoons
    }
    return render(request, 'webtoon/webtoon_list.html', context)


def episode_detail(request, pk):
    context= {
        'post': Episode.objects.get(pk=pk),
    }
    return render(request, 'episode/episode_detail.html', context)

