from email.policy import default
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    owner = models.ForeignKey(get_user_model(),  
        on_delete=models.CASCADE
    )
    done = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("home")
    