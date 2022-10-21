from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class ArtistList(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_serializer_context(self):
        return {'request': self.request}
