from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class Inciar_secion(LoginView):
    template_name = '' 
    success_url = reverse_lazy('')
