from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from core.views import GroupViewSet, UserViewSet
from list.views import ItemViewSet, ListViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"items", ItemViewSet)
router.register(r"lists", ListViewSet, basename="list")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-token-auth", views.obtain_auth_token, name="api-token-auth"),
]
