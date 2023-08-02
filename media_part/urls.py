from django.urls import path
from .views import PostViewSet
from .views import EditPostView
from .views import AddPostView
from .views import LikesView
from .views import AddLikeView





urlpatterns = [
    path('api/v1/post/', PostViewSet.as_view({'get': 'list'})),
    path('api/v1/add_post/', AddPostView.as_view()),
    path('api/v1/edit_post/<int:pk>/', EditPostView.as_view({"get":"retrieve",
                                                             "put":"update",
                                                             "delete":"destroy",
                                                             })),
    path('api/v1/likes_list/<int:pk>/', LikesView.as_view()),
    path('api/v1/add_like/<int:pk>/', AddLikeView.as_view(), name='add_likes'),
]


