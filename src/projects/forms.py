from django.forms import ModelForm

from .models import Category, Project


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description')


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'is_mental', 'is_physical')


class UpdateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'is_mental', 'is_physical', 'is_done', 'category')

