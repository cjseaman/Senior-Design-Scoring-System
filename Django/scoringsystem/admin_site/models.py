from django.db import models

# Create your models here.
class Session(models.Model):
	sessionNumber = models.AutoField(primary_key=True)
	addJudge = models.ForeignKey('users.User', on_delete=models.CASCADE, name='Add Judge')
	addStudent = models.ForeignKey('admin_site.Student', on_delete=models.CASCADE, name='Add Student')

	def __str__(self):
		return str(self.sessionNumber)

class Student(models.Model):
	name = models.CharField(max_length=255)
	eDiscipline = models.CharField(max_length=255)

	def __str__(self):
		return self.name# + '-' + self.eDiscipline