from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('artists', views.ArtistViewSet)
urlpatterns = router.urls
