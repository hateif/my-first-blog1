from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField()

class Teacher(models.Model):
	name = models.CharField(max_length = 50)
	age = models.IntegerField()
	
class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	
class Choice(models.Model):
	
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)