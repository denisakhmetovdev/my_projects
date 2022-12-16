from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from django.views.generic import ListView

from projects.models import Category, Project


# def home(request):
#     time_now = timezone.localtime(timezone.now()) + timedelta(hours=6)
#     context = {
#         'time_now': time_now
#     }
#     return render(request, 'main_app/home.html', context)


class CategoryList(ListView):
    model = Category
    template_name = 'main_app/home.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_done=False).order_by('category', '-is_mental')
        return context
