from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView, CreateView, UpdateView, DeleteView
from datetime import datetime

from .models import Category, Project, Task, ProjectComment, ProjectStatus, Subtask, SubtaskComment, TaskComment
from .forms import CategoryForm, ProjectForm, UpdateProjectForm


class CategoryDetail(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(category=self.kwargs['pk']).order_by('-is_mental')
        return context


class ProjectDetail(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data()
        context['tasks'] = Task.objects.filter(project=self.kwargs['pk'])
        context['status'] = ProjectStatus.objects.filter(project=self.kwargs['pk']).last()
        context['comment'] = ProjectComment.objects.filter(project=self.kwargs['pk']).filter(to_archive=False).last()
        return context


class AddCategory(CreateView):
    form_class = CategoryForm
    template_name = 'projects/add_category.html'
    success_url = '/projects/add_category/'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        return context


class AddProject(CreateView):
    form_class = ProjectForm
    template_name = 'projects/add_project.html'
    success_url = '/projects/category/{category_id}/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs['category_id'])
        context['projects'] = Project.objects.filter(category=category)
        context['category'] = category
        return context

    def form_valid(self, form, **kwargs):
        post = form.save(commit=False)
        post.category = Category.objects.get(pk=self.kwargs['category_id'])
        post.save()
        return super().form_valid(form)


class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = '/projects/add_category/'


class UpdateProject(UpdateView):
    model = Project
    form_class = UpdateProjectForm
    success_url = '/projects/category/{category_id}/add_project/'


class DeleteCategory(DeleteView):
    model = Category
    success_url = '/projects/add_category/'


class DeleteProjectView(DeleteView):
    model = Project
    success_url = '/projects/category/{category_id}/add_project/'
