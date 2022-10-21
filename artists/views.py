from django.shortcuts import render
from django.views import View
from artists.models import Artist
from .forms import ArtistForm

# Create your views here.


class create(View):
    form_class = ArtistForm
    initial = {'key': 'value'}
    template_name = 'createArtist.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})


class list(View):
    template_name = 'listArtist.html'

    def get(self, request):
        return render(request, self.template_name, {'query_set': Artist.objects.all().prefetch_related('album_set')})
