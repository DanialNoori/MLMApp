from django.db import models
from users.models import AppUser
# Create your models here.


class Task(models.Model):
	roles = (('q' , 'qualify'), ('b' , 'bronze'), ('silver', 'silver'), ('g','gold'), ('p', 'platinium'))
	associtedWithRole = models.CharField(max_length=10, choices=roles, blank=True, null=True, 
		verbose_name='Associated With Role:')
	number = models.IntegerField(blank=True, null=True, verbose_name='Number of Role:')
	name = models.TextField(verbose_name='Name')
	description = models.TextField(verbose_name='Description')
	audioFile = models.FileField(upload_to='audio_files/' , verbose_name='Audio File', blank=True, null=True)
	examScore = models.IntegerField(blank=True, null=True, verbose_name='Exam Score')

	def __str__(self):
		return self.name


class Scheduler(models.Model):
	validChoice = (('accepted' , 'Accepted'),
		('pending' , 'Pending'),
		('rejected' , 'Rejected'))

	user = models.ForeignKey(AppUser, verbose_name='User')
	task = models.ForeignKey(Task, verbose_name='Task')
	accomplished = models.BooleanField(default=False, verbose_name='Accomplished?')
	accepted = models.CharField(default='pending', verbose_name='Accept', choices=validChoice, max_length=20,)

	def __str__(self):
		return self.user.user.username