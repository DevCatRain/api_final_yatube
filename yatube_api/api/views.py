from rest_framework import viewsets, filters, mixins
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, User, Follow
from .serializers import (FollowSerializer, PostSerializer, GroupSerializer,
                          CommentSerializer, UserSerializer)
from .permissions import IsAuthorOrReadOnly


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    pass


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class UpdateDestroyViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):

    """ Предоставляет возможность работать с постами:
    создавать, редактировать, удалять.
    Координирует разрешения на доступ.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """ Дает возможность использовать базу User.
    Работает только на чтение.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    """ Предоставляет возможность создавать группы.
    Координирует разрешения на доступ.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly,)


class CommentViewSet(CreateListRetrieveViewSet, UpdateDestroyViewSet):

    """ Предоставляет возможность работать с комментариями:
    создавать, редактировать, удалять.
    Координирует разрешения на доступ.
    """

    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = CommentSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        commets = post.comments.all()
        return commets

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user, post=get_object_or_404(
                Post, id=self.kwargs['post_id']
            )
        )


class FollowViewSet(CreateListViewSet):

    """ Предоставляет возможность создавать подписки.
    Дает возможность поиска по автору и подписчику.
    """

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username', '=user__username')
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset
