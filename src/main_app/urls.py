from django.urls import path

from .views import CategoryList  #home


urlpatterns = [
    path('', CategoryList.as_view(), name='home')
]
