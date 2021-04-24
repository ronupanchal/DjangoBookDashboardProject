import datetime

from django.db import models

# Create your models here.


class Event(models.Model):
    """Model representing a calendar event (e.g. Workshop, Seminar)."""
    start = models.DateTimeField(default=datetime.datetime.now())
    end = models.DateTimeField(default=datetime.datetime.now())

    eventname = models.CharField(
        max_length=200,
        help_text="Enter a event name (e.g. Workshop, Seminar etc.)"
        )
    uid = models.IntegerField()

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.eventname





