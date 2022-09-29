from django.shortcuts import redirect, render
from .forms import StudentDetailsForm
from .models import StudentDetails
# Create your views here.
def Home(request):
    data=StudentDetails.objects.all() 
    return render(request,'index.html',{'data1':data})

def Register(request):
    form = StudentDetailsForm()
    if request.method == 'POST':
        form1=StudentDetailsForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'register.html',context)

def Update(request,pk):
    data = StudentDetails.objects.get(id=pk)
    form = StudentDetailsForm(instance=data)
    context={'form':form}
    if request.method == 'POST':
        form1= StudentDetailsForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,'register.html',context)

def DeleteUser(request,pk):
    data = StudentDetails.objects.get(id=pk)
    data.delete()
    return redirect('home')

