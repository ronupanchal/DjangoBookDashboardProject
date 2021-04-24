from django.forms import models
from .models import Event


class EventForm(models.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"