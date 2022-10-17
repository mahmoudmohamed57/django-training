from django.shortcuts import render
from .forms import AlbumForm

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm()
    return render(request, 'createAlbum.html', {'form': form})
