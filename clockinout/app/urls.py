from django.urls import path, include

from . import views
app_name = 'app'
urlpatterns = [
	path('', views.index, name='index'),
	path('list-events', views.list_events, name='list-events'),
	path('process-clock-event', views.process_clock_event,
		name='process_clock_event'),
]