from django.urls import path
from rest_framework import routers

from .views import PostViewSet, like_post, CommentViewSet, read_post

router = routers.SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls + [
    path('like/<int:pk>/', like_post, name='like_post'),
    path('read/<int:pk>/', read_post, name='read_post')
]