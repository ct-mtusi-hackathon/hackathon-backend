from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from src.apps.users.api.views import UserProfileViewSet


router = SimpleRouter()
router.register("users", UserProfileViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("api/v1/", include(router.urls))]
