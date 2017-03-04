from django.db import models

# Create your models here.
class Front(models.Model):
	
	name=models.CharField(max_length=120,blank=False,null=False)
	clss=models.CharField(max_length=6,blank=False,null=False)
	mark1=models.IntegerField()
	mark2=models.IntegerField()
	mark3=models.IntegerField()
	rollno=models.IntegerField()
	avg=models.IntegerField()
	
	def _unicode_(self):
		return self.name