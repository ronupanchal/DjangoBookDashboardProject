from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views import View
from .forms import EventForm
from calendarapp.models import Event

import datetime

# Create your views here.
def calview(request):
    title ="cal View"
    start = datetime.date.today()
    return render(request, 'calendarui/calender_demo.html', {'title': title, 'start': start})


class EventView(View):

    def get(self, request):
        form = EventForm()
        return render(request, 'calendarui/calender_ui.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data['eventname'])
                form.save()
                return redirect('calendar:CalenderList')


class EventList(DetailView):
    model = Event
    template_name = 'calendarui/calender_ui.html'
    print(id)

   # context_object_name = 'events'


class CalendarView(TemplateView):

     template_name = 'calendarui/calender_ui.html'


# user type and username


# add schedule


# add event or task


#





# def index(request):
#     title ="Dashboard"
#     context={
#         'title': title,
#     }
#     return render(request, 'calendarui/basic_calender.html', context )

#
#
# class CalendarJsonListView(ListView):
#
#     template_name = 'django_bootstrap_calendar/calendar_events.html'
#
#     def get_queryset(self):
#         queryset = CalendarEvent.objects.filter()
#         from_date = self.request.GET.get('from', False)
#         to_date = self.request.GET.get('to', False)
#
#         if from_date and to_date:
#             queryset = queryset.filter(
#                 start__range=(
#                     timestamp_to_datetime(from_date) + datetime.timedelta(-30),
#                     timestamp_to_datetime(to_date)
#                     )
#             )
#         elif from_date:
#             queryset = queryset.filter(
#                 start__gte=timestamp_to_datetime(from_date)
#             )
#         elif to_date:
#             queryset = queryset.filter(
#                 end__lte=timestamp_to_datetime(to_date)
#             )
#
#         return event_serializer(queryset)
#
#
# class CalendarView(TemplateView):
#
#     template_name = 'django_bootstrap_calendar/calendar.html'