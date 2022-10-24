from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Task

#Class-based views
class HomePageView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super(HomePageView ,self).get_context_data(**kwargs)
        context['active'] = Task.objects.filter(done=False)
        context['finish'] = Task.objects.filter(done=True)

        return context


class TaskCreateView(LoginRequiredMixin ,CreateView):
    login_url = 'login'
    model = Task
    fields = ['title']
    template_name = 'task_new.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


#view functions
@login_required
def updateTaskStatusView(request, pk):
    """ Change the status of a task from active to finished. """

    task = Task.objects.get(pk=pk)

    #Check if the owner of the task is making the request.
    if task.owner != request.user:
        raise PermissionDenied

    #Update and save the new status
    task.done = True
    task.save()

    #redirect the user to the home page
    return HttpResponseRedirect(reverse('home'))

    


