from django.db import models
from django.urls import reverse
class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва категорії')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    
class Create_Post(models.Model):
    name = models.CharField(max_length=200, verbose_name='Назва зображення / теми')
    photo = models.ImageField(null=False, verbose_name='Зображення')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    description = models.TextField(null=True, verbose_name='Опис')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('picture_detail', kwargs={'photo_id': self.pk})

    def get_related_posts(self):
        return Create_Post.objects.filter(category=self.category).exclude(pk=self.pk)

    class Meta:
        verbose_name = 'Добавити пост'
        verbose_name_plural = 'Добавити пост'



