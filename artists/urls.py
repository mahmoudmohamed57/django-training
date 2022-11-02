from rest_framework_nested import routers
from . import views


router = routers.SimpleRouter()
router.register('artists', views.ArtistList)

urlpatterns = router.urls
