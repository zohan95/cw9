from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from rest_framework import viewsets, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CommentSerializer, PhotoSerializer
from webapp.models import Comment, Photo


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS or self.request.method == 'POST':
            return []

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        comment = Comment(author=User.objects.get(username=data['author']), photo=Photo.objects.get(pk=data['photo']),
                          text=data['text'])
        comment.save()
        return Response({'text': comment.text, 'author': comment.author.username, 'date_create': comment.date_create,
                         'id': comment.id}, status=status.HTTP_200_OK)

    # def get_permissions(self):
        # if self.request.method in SAFE_METHODS or self.request.method == 'POST':
        #     return []
        # if self.action in ['destroy']:
        #     return [IsAuthenticated, DjangoModelPermissions]
        # if self.action in ['update', 'partial_update']:
        #     obj = self.get_object()
        #     if obj.author != self.request.user or self.request.user.has_perm('webapp:delete_comment'):
        #         return [AllowAny]
        # return [IsAuthenticated]


class PhotoViewSet(viewsets.ModelViewSet, DjangoModelPermissions):
    permission_classes = [DjangoModelPermissions, IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS or self.request.method == 'POST':
            return []

        return super().get_permissions()


class RateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=kwargs['pk'])
        operation = request.data['operation']
        if operation == 'plus':
            if User.objects.get(username=request.data['user']) in photo.liked.all():
                return Response(status.HTTP_403_FORBIDDEN)
            else:
                photo.likes = photo.likes + 1
                photo.liked.add(User.objects.get(username=request.data['user']))
        else:
            if User.objects.get(username=request.data['user']) not in photo.liked.all():
                return Response(status.HTTP_403_FORBIDDEN)
            else:
                photo.likes = photo.likes - 1
                photo.liked.remove(User.objects.get(username=request.data['user']))
        photo.save()
        return JsonResponse({'newlike': photo.likes})
