from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Picture(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='user_pics', verbose_name='Картинка')
    title = models.CharField(max_length=50, null=False, blank=True, verbose_name='Подпись')
    uploaded = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='author', verbose_name='Автор')



    def __str__(self):
        return f'{self.photo } - {self.title}'

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Favorites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='user', verbose_name='Пользователь')
    fav_picture = models.ManyToManyField('webapp.Picture', related_name='fav_picture', blank=True, verbose_name='Избранное фото')

    def __str__(self):
        return f'{self.user.username} - {self.fav_picture}'

    class Meta:
        verbose_name = 'Избранное фото'
        verbose_name_plural = 'Избранные фото'

