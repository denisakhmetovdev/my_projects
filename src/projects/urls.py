from django.urls import path

from .views import CategoryDetail, ProjectDetail, AddCategory, AddProject, UpdateProject, UpdateCategory, \
    DeleteCategory, DeleteProjectView


urlpatterns = [
    # path('', home, name='home'),
    path('category/<int:pk>/delete/', DeleteCategory.as_view(), name='delete_category'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('add_category/update/<int:pk>/', UpdateCategory.as_view(), name='update_category'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('category/<int:category_id>/delete_project/<int:pk>/', DeleteProjectView.as_view(), name='delete_project'),
    path('category/<int:category_id>/add_project/update/<int:pk>/', UpdateProject.as_view(), name='update_project'),
    path('category/<int:category_id>/add_project/', AddProject.as_view(), name='add_project'),
]
