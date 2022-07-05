from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length=200,null=False)
	location = models.CharField(max_length=200)
	def __str__(self):
		return self.name
		
class Role(models.Model):
	role = models.CharField(max_length=100)
	def __str__(self):
		return self.role

class Employee(models.Model):
	first_name = models.CharField(max_length=50,null=False)
	last_name = models.CharField(max_length=20)
	dept = models.ForeignKey(Department,on_delete=models.CASCADE)
	salery = models.IntegerField(default=0)
	bonus = models.IntegerField(default=0)
	# role = models.ForeignKey(Role,on_delete=models.CASCADE)
	phone = models.IntegerField(default=0)
	hire_date = models.DateField()
	def __str__(self):
		return self.first_name