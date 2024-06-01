from django.shortcuts import render,redirect
from django.core.mail import send_mail

from . models import Employee

# Create your views here.
def index(request):
    return render(request,'index.html')


def read(request):
    emp = Employee.objects.all()
    send_mail('Welcome','Thank you for visiting site',
              'jadhavnilesh7479@gmail.com',['poojachaudhari8450@gmail.com'],fail_silently=False)
   
    return render(request,'index.html', {'emp':emp})




def add(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")

    emp = Employee(
        name = name,
        email = email,
        address = address,
        phone = phone,
    )

    emp.save()
    return redirect('/')




def edit(request):
    emp = Employee.objects.all()    
    context = {
        'emp':emp
    }
    return redirect('/',context)


def update(request,id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")


        emp = Employee(
        id = id,
        name = name,
        email = email,
        address = address,
        phone = phone,
        )

        emp.save()
        return redirect('/') 


def delete(request,id):
    emp = Employee.objects.filter(id = id)
    emp.delete()
    return redirect('/')

def delete_all(request):
    emp = Employee.objects.all()
    return redirect('/')


