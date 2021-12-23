from django.db import models
from django.urls import reverse


class Producer(models.Model):
    name = models.CharField(max_length=300, verbose_name='Производитель')
    slug = models.CharField(max_length=300, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Goods(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Описание')
    number_of_goods = models.IntegerField(verbose_name='Количество товаров на складе')
    manufactured = models.ForeignKey(Producer, on_delete=models.CASCADE, verbose_name='Производитель')
    date_of_addition = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    price = models.FloatField(verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

