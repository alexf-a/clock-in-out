from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import Clock, ClockForm

def index(request):
	context = {}
	context['clock_form'] = ClockForm()
	return render(request, 'app/index.html', context)

def list_events(request):
	clock_events = Clock.objects.order_by('-date_time')
	context = { 'event_list': clock_events }
	return render(request, 'app/list-events.html', context)
	
def process_clock_event(request):
	if request.method == "POST":
		data = request.POST
		teacher = data["user"]
		type = data["type"]
		form = ClockForm(data=data)
		if form.is_valid():
			clock_event = form.save()
		else:
			raise Http404("Invalid form submission. Please try again.")
	return HttpResponseRedirect('/app')