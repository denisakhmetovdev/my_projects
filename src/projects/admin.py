from django.contrib import admin

from .models import Category, Project, ProjectComment, ProjectStatus, Task, TaskComment, Subtask, SubtaskComment


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ProjectComment)
admin.site.register(ProjectStatus)
admin.site.register(Task)
admin.site.register(TaskComment)
admin.site.register(Subtask)
admin.site.register(SubtaskComment)
