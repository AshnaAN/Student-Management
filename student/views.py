from django.shortcuts import render
import datetime
from student.models import *
# Create your views here.

def home(request):
	return render(request, "front.html", {})


#def signfun(request):
#	print 'hi'
#	print request.POST
#	first_name = request.POST['name']
#	passwd = request.POST['password']
#	s = SignUp(name = first_name, password = passwd)
	# s = SignUp()
	# s.name = first_name
	# s.password = passwd
#	s.save()
#	print first_name, passwd	
#	return render(request, "contact_us.html", {})	

#def contactus(request):
#	print request.POST
#	return render(request, "home.html",{})

def suces(request):
	print request.POST
	st_name = request.POST['name']
	rol = request.POST['rollno']
	Cls =request.POST['clss']
	m1 = request.POST['mark1']
	m1=int(m1)
	m2 = request.POST['mark2']
	m2=int(m2)
	m3 = request.POST['mark3']
	m3=int(m3)
	av=m1+m2+m3
	averge=av/3
	st = Front(name = st_name, rollno = rol, clss = Cls, mark1 = m1, mark2 = m2, mark3 = m3 , avg = averge)
	print st.avg

	st.save()

	return render(request,"sucessful.html",{})

def viewing(request):
	
     

	# s = Front.objects.filter(mark1__gt=80 ,mark2__gt=80 ,mark3__gt=80)
	s=Front.objects.all()

	student_details = []

	for i in s:
		d = {}
		d['name'] = i.name
		d['clss'] = i.clss
		d['mark1'] = i.mark1
		d['mark2'] = i.mark2
		d['mark3'] = i.mark3
		d['avg'] = i.avg
		student_details.append(d)

	return render(request,"view.html", {'details':student_details})




