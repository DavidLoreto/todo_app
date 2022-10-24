from django.urls import path

from .views import HomePageView, updateTaskStatusView, TaskCreateView


urlpatterns = [
    #Home page
    path('', HomePageView.as_view(), name='home'),
    
    #Update task status
    path('<int:pk>/update/', updateTaskStatusView, name='task_update'),

    #Add a new task
    path('new/', TaskCreateView.as_view(), name='task_new')
]
