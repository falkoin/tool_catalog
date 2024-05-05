from rest_framework import routers

from api.viewsets import ToolViewSet

router = routers.SimpleRouter()
router.register(r'tools', ToolViewSet)

urlpatterns = router.urls

