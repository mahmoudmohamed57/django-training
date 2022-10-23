from .models import Album, Song
from .serializers import AlbumSerializer, SongSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(ModelViewSet):
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs['album_pk'])

    def get_serializer_context(self):
        return {'album_id': self.kwargs['album_pk']}
