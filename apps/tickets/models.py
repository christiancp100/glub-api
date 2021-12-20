from django.db import models

from apps.accounts.models import User
from apps.events.models import Event

"""
class TicketType(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=120, blank=False)
    num_tickets = models.IntegerField(default=0)
    #TODO Add drinks


    def __str__(self):
        return f'{self.name} para {self.event.name}'
        
"""


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    is_ticked = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
