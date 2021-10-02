from django.db import models
from apps.accounts.models import User
from apps.bars.models import Bar


class Registry(models.Model):
    date_registered = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
