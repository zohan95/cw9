from webapp.models import Comment, Photo

from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    comment_photo = CommentSerializer(many=True)

    class Meta:
        model = Photo
        fields = '__all__'
