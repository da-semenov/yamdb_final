import datetime

from django.core import validators
from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='Slug категории',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название жанра',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='Slug жанра',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True,
        blank=False
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        validators=(
            validators.MinValueValidator(1895),
            validators.MaxValueValidator(datetime.date.today().year)
        ),
        blank=True,
        null=True,
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles',
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name='Категория',
        related_name='titles',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(blank=False, verbose_name='Отзыв')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        db_index=True
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        validators=(
            validators.MinValueValidator(1),
            validators.MaxValueValidator(10)
        )
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:100]


class Comment(models.Model):
    text = models.TextField(blank=False, verbose_name='Комментарий')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        db_index=True
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:100]
