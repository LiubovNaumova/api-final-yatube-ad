from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r"posts", PostViewSet, basename="posts")
router_v1.register(r"groups", GroupViewSet, basename="groups")
router_v1.register(r"follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/", include("djoser.urls.jwt")),
    path(
        "v1/posts/<int:post_id>/comments/",
        CommentViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="comments-list",
    ),
    path(
        "v1/posts/<int:post_id>/comments/<int:pk>/",
        CommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="comments-detail",
    ),
]
