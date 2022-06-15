from django.db import models
from django.urls import reverse


class Picture(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Загружено')
    image = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_pic', kwargs={'pk': self.pk})
