from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Тег', max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    content = models.TextField('Текст')
    image = models.ImageField('Картинка', upload_to='articles/', blank=True, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    views = models.PositiveIntegerField('Просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Book(models.Model):
    title = models.CharField('Название', max_length=200)
    author = models.CharField('Автор', max_length=150)
    genre = models.CharField('Жанр', max_length=100)
    description = models.TextField('Описание')
    cover = models.ImageField('Обложка', upload_to='books/', blank=True, null=True)
    avidreaders_url = models.URLField('Ссылка на AvidReaders', blank=True)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    def __str__(self):
        return f'{self.author} — {self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']


