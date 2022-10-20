from django.shortcuts import render
from django.views import View
from .forms import AlbumForm

# Create your views here.


class create(View):
    form_class = AlbumForm
    initial = {'key': 'value'}
    template_name = 'createAlbum.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})
