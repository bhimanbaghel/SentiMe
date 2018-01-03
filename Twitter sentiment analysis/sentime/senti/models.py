from django.db import models

# Create your models here.

class People(models.Model):
	people_name = models.CharField(max_length=30)
	def __str__(self):
		return self.people_name
	people_positive = models.IntegerField(default=0)
	people_negative = models.IntegerField(default=0)
	people_neutral = models.IntegerField(default=0)