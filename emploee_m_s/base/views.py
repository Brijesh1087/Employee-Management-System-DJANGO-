from django.shortcuts import render,redirect,HttpResponse
from .models import Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
	emps = Employee.objects.all()
	# print(dir(request))
	# print(request.path)
	return render(request,'index.html',{'emps':emps})

def add_emps(request):
	if(request.method=="POST"):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		dept = int(request.POST['dept'])
		salery = int(request.POST['salery'])
		bonus = int(request.POST['bonus'])
		phone = int(request.POST['phone'])
		emsps = Employee(first_name=first_name,last_name=last_name,dept_id=dept,salery=salery,bonus=bonus,phone=phone,hire_date=datetime.now())
		emsps.save()
		return redirect("/")
	else:
		return render(request,'add_emps.html')

def rem_emps(request,emps_id=0):
	emps = Employee.objects.all()
	if emps_id:
		try:
			del_emps = Employee.objects.get(id=emps_id)
			del_emps.delete()
			return redirect("/")
		except:
			return render(request,'remove.html',{'emps':emps})
	else:
		emps = Employee.objects.all()
		return render(request,'remove.html',{'emps':emps})

def filter(request):
	if(request.method=='POST'):
		search = request.POST['search']
		emps = Employee.objects.all()
		emps = emps.filter(Q(first_name__icontains=search) |Q(last_name__icontains=search)  )
		if isinstance(search,int):
			emps = emps.filter(dept_id=search)
		return render(request,'index.html',{'emps':emps})
	else:
		return render(request,'filter.html')