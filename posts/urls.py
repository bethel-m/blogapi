from posixpath import basename
from django.urls import path
#from .views import PostList, PostDetail, UserDetail, UserList
from .views import UserViewSet,PostViewSet
from rest_framework.routers import SimpleRouter

"""
urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("",PostList.as_view(), name="post_list"),
    path("",PostList.as_view()),
    path("users/", UserList.as_view()),
    path("users/<int:pk>", UserDetail.as_view()),
]
"""

# the routers below function same as the urlpatterns above

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("",PostViewSet,basename="posts")

urlpatterns = router.urls