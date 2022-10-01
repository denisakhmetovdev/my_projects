from django.urls import path

from main_app.views import home


urlpatterns = [
    path('', home, name='home')
]
