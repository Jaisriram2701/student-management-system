from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    data  = StudentsModel.objects.all()
    return render(request,'home.html',{'data':data})
    
def about(request):
    return render(request,'about.html')
def add_student(request):
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['roll_number']
        c=request.POST['email']
        d=request.POST['department']
        e=request.POST['dob']

        print(a,b,c,d,e)

        StudentsModel.objects.create(
            name=a,
            roll_number=b,
            email=c,
            department=d,
            dob=e
        )
        
    return render(request,'add_student.html')

def update(request,pk):
    data = StudentsModel.objects.get(id=pk)

    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['roll_number']
        c = request.POST['email']
        d = request.POST['department']
        e = request.POST['dob']
        # print(a,b,c,d,e)
        data.name = a
        data.roll_number = b
        data.email = c
        data.department = d
        data.dob = e
        data.save()
        messages.success(request, "Record updated successfully")   
        return redirect('home') 
         
    return render(request,'update.html',{'data':data})

def trash(request):
    data = TempModel.objects.all()
    return render(request, 'trash.html', {'data': data})


def delete(request, pk):
    student = StudentsModel.objects.get(id=pk)

    # Move to TempModel
    TempModel.objects.create(
        name=student.name,
        roll_number=student.roll_number,
        email=student.email,
        department=student.department,
        dob=student.dob
    )

    # Delete from StudentsModel
    student.delete()
    messages.success(request, "Record removed successfully")
    return redirect('home')

def restore(request, pk):
    student = TempModel.objects.get(id=pk)

    # Move back to StudentsModel
    StudentsModel.objects.create(
        name=student.name,
        roll_number=student.roll_number,
        email=student.email,
        department=student.department,
        dob=student.dob
    )

    # Remove from TempModel
    student.delete()
    messages.success(request, "Record restored successfully")
    return redirect('trash')

def permanent_delete(request, pk):
    student = TempModel.objects.get(id=pk)
    student.delete()
    messages.success(request, "Permanently deleted successfully")
    return redirect('trash')