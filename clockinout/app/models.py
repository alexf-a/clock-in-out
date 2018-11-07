from django.db import models
from django.forms import ModelForm

class User(models.Model):
	''' An abstract base class to represent a user.
	Attributes:
	 - first_name -- A string to represent this User's first name.
	 - last_name -- A string to represent this User's last name. 
	'''
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.first_name + " " + self.last_name
		
	class Meta:
		abstract = True

class Teacher(User):
	''' A class to represent a teacher. Inherits from abstract User.
	Attributes:
	 - name -- A string to represent this Teacher's name.
	'''
	pass
	
	
class Clock(models.Model):
	''' A class to represent a clock-event by a Teacher.
	Attributes:
	- date_time -- The date and time of the clock-event.
	- type -- Two-option string field for whether the Teacher clocked in or out. 
	- user -- The Teacher who clocked in or out.
	'''
	TYPE_CHOICES = (
		('IN', 'Clock-In'),
		('OUT', 'Clock-Out')
	)
	date_time = models.DateTimeField('Clock-event time', auto_now_add=True)
	type = models.CharField(max_length=3, choices=TYPE_CHOICES)
	user = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.user) + " Clocked-" + self.type + " on " + str(self.date_time)
		
class ClockForm(ModelForm):
	'''A Form class for clocking in or out with a Clock event. '''
	class Meta:
		model = Clock
		fields = ('user', 'type')