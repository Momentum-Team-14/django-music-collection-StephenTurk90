from django.shortcuts import render
from django.utils import timezone
from .models import Album


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums':albums})
