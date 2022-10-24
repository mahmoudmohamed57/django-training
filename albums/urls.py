from . import views
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('albums', views.AlbumViewSet)
songs_router = routers.NestedSimpleRouter(router, 'albums', lookup='album')
songs_router.register('songs', views.SongViewSet, basename='album-songs')


urlpatterns = router.urls + songs_router.urls
