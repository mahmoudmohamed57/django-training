from django.shortcuts import render
from artists.models import Artist
from .forms import ArtistForm

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtistForm()
    return render(request, 'createArtist.html', {'form': form})


def list(request):
    return render(request, 'listArtist.html', {'query_set': Artist.objects.all().prefetch_related('album_set')})
