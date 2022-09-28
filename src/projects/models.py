from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProjectName(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class ProjectStatus(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Статус проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class BooleanStatus(models.Model):
    title = models.CharField(max_length=60, verbose_name='Характеристика')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    projects_status = models.ForeignKey(ProjectName, on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name = 'Bool-характеристика'
        verbose_name_plural = 'Bool-характеристики'


class TextStatus(models.Model):
    title = models.CharField(max_length=100, verbose_name='Характеристика')
    description = models.CharField(max_length=255, verbose_name='Статус')
    project_status = models.ForeignKey(ProjectName, on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name = 'Текстовая характеристика'
        verbose_name_plural = 'Текстовые характеристики'
