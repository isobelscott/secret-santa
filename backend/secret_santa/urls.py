from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, PartyViewSet, GroupViewSet

router = DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'parties', PartyViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = router.urls
