from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def webtoon_list(request):

    webtoons = Webtoon.objects.all()
    context = {
        'webtoons':webtoons
    }
    return render(request, 'webtoon/webtoon_list.html', context)




# def webtoon_detail(request, pk):
#
#     webtoon_details = Webtoon.objects.get(pk=pk)
#     context={
#         webtoons
#     }
def episode_list(request):

    episodes = Episode.objects.all()
    context= {
        'episodes': episodes
    }
    return render(request, 'episode/episode_list.html', context)




def episode_detail(request, pk):

    episodes = Episode.objects.get(pk=pk)
    context= {
        'episodes': episodes
    }
    return render(request, 'episode/episode_detail.html', context)
