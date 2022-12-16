from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile_detail.html'
