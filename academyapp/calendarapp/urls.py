from django.urls import path
from . import views
app_name = 'calendar'

urlpatterns =[
    path('toastui/', views.calview, name='calview'),
    path('', views.EventView.as_view(), name='CalenderView'),
    path('', views.EventList.as_view(), name='CalenderList'),
    path('',views.EventView)
    #path('', views.calview, name='CalenderView'),
]