from .models import Album
from .serializers import AlbumSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class AlbumList(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_serializer_context(self):
        return {'request': self.request}
