from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    model = CustomUser
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

