from django.shortcuts import render
from django.utils import timezone
from .models import Album


def album_list(request):
    albums = Album.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'albums/album_list.html', {})
