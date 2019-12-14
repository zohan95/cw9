from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import CommentSerializer, PhotoSerializer
from webapp.models import Comment, Photo


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        data = request.data
        comment = Comment(author=User.objects.get(username=data['author']), photo=Photo.objects.get(pk=data['photo']), text=data['text'])
        comment.save()
        return Response({'text':comment.text, 'author':comment.author.username, 'date_create': comment.date_create,'id':comment.id}, status=status.HTTP_200_OK)



class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class RateView(APIView):
    permission_classes = [AllowAny, ]

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
