from math import ceil
from django.shortcuts import render
from . import models
from core.libs import core


def all_rooms(request):
    page_size = 10
    page_per_block = 10

    page = request.GET.get('page', 1)

    paging = core.paging(models.Room, page, page_size, page_per_block)
    
    return render(request, "rooms/home.html", {'paging': paging})
