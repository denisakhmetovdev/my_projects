from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_mental = models.BooleanField(verbose_name='Ментальная задача')
    is_physical = models.BooleanField(verbose_name='Физическая задача')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    changed = models.DateTimeField(auto_now=True, verbose_name='Изменён')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def set_changed(self):
        if not self.changed:
            self.changed = self.created

    def __str__(self):
        return self.title


class ProjectComment(models.Model):
    """Проверить str для строки менее 40 знаков"""
    title = models.CharField(max_length=250, blank=True, verbose_name='Заголовок')
    comment = models.TextField(verbose_name='Комментарий')
    to_archive = models.BooleanField(verbose_name='Архивировать')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Комментарий к проекту'
        verbose_name_plural = 'Комментарии к проекту'

    def __str__(self):
        if len(str(self.title)) > 40:
            return f'{self.comment[:40]}...'
        else:
            return self.title


class ProjectStatus(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Статус проекта')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')

    class Meta:
        verbose_name = 'Общий статус (commit проекта)'
        verbose_name_plural = 'Общие статусы (commit\'ы проекта)'

    def __str__(self):
        if len(str(self.title)) > 35:
            return f'{self.title[:35]}...'
        else:
            return self.title


class Task(models.Model):
    title = models.CharField(max_length=60, verbose_name='Характеристика')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    to_be_done_by_date = models.DateField(blank=True, null=True, verbose_name='Сделаю к дате')
    to_be_done_in_time = models.TimeField(blank=True, null=True, verbose_name='Сделаю ко времени')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Задача создана')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        if len(str(self.title)) > 30:
            return f'{self.title[:30]}...'
        else:
            return self.title


class TaskComment(models.Model):
    """Проверить str для строки менее 40 знаков"""
    title = models.CharField(max_length=250, blank=True, verbose_name='Заголовок')
    comment = models.TextField(verbose_name='Комментарий')
    to_archive = models.BooleanField(verbose_name='Архивировать')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Проект')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задаче'

    def __str__(self):
        return f'{self.comment[:40]}...'


class Subtask(models.Model):
    title = models.CharField(max_length=60, verbose_name='Характеристика')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задача')
    to_be_done_by_date = models.DateField(blank=True, null=True, verbose_name='Сделаю к дате')
    to_be_done_in_time = models.DateField(blank=True, null=True, verbose_name='Сделаю ко времени')
    created = models.DateTimeField(auto_now_add=True, verbose_name=' Подзадача создана')

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'

    def __str__(self):
        return f'{self.title[:30]} | К задаче: {self.task.__str__()}'


class SubtaskComment(models.Model):
    """Проверить str для строки менее 40 знаков"""
    title = models.CharField(max_length=250, blank=True, verbose_name='Заголовок')
    comment = models.TextField(verbose_name='Комментарий')
    to_archive = models.BooleanField(verbose_name='Архивировать')
    subtask = models.ForeignKey(Subtask, on_delete=models.CASCADE, verbose_name='Проект')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name = 'Комментарий к подзадаче'
        verbose_name_plural = 'Комментарии к подзадаче'

    def __str__(self):
        return f'{self.comment[:40]}...'
