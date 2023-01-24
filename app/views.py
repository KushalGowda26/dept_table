from django.shortcuts import render
from app.models import *
# Create your views here.
def display_emp(request):
  QST=Emp.objects.all()
  d={ 'emp':QST }
  
  return render(request,'emp_details.html',context=d)


def display_dept(request):
  QST=Dept.objects.all()
  d={ 'dept':QST }
  
  return render(request,'dept_details.html',context=d)