from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from user.models import User

# Create your views here.
class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = 'user/list.html'
    permission_required = 'user.view_user'
    data = []


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['entity'] = 'Usuarios'
        return context
