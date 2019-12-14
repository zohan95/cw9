from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(verbose_name='Фотография', upload_to='')
    sign = models.CharField(max_length=63, verbose_name='Подпись')
    date_create = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT, related_name='photo_user', null=False, blank=True)
    liked = models.ManyToManyField(User, related_name='user_love', blank=True)

    def __str__(self):
        return self.sign[:10]


class Comment(models.Model):
    text = models.TextField(max_length=255, verbose_name='Комментарий')
    photo = models.ForeignKey(Photo, verbose_name='Фотография', on_delete=models.CASCADE, related_name='comment_photo')
    author = models.ForeignKey(User, verbose_name='Автор', related_name='comment_author', on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:10]







