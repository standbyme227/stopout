from django.shortcuts import render
from .models import *

def webtoon_list(request):

    webtoons = Webtoon.objects.all()
    context = {
        'webtoons':webtoons
    }
    return render(
        request, ''
    )


