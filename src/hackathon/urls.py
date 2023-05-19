from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from src.apps.users.api.views import UserProfileViewSet
from src.apps.events.api.views import EventViewSet


router = SimpleRouter()
router.register("users", UserProfileViewSet)
router.register("events", EventViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/", include("src.apps.base.api.urls")),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/", include("src.apps.auth.api.urls")),
    path(
        "api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"
    ),
]
