from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import CreateUserForm,LoginForm,AddRecordForm,UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from.models import Record
from django.contrib import messages
# Create your views here.

# home view
def home(request):
    return render(request, 'Student/index.html')

# register view for registering

def register(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created succesfully")

        return redirect('my-login')

    context ={'form':form}
    return render (request,'Student/register.html',context=context)



# login view
def mylogin(request):
    form = LoginForm()
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(request,username=username, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, "Account created succesfully")

                return redirect("dashboard")
    
    context={'form':form}

    return render (request, 'Student/my-login.html',context)


# user logout

def my_logout(request):
    auth.logout(request)
    messages.success(request," User logged out ")
    return redirect("my-login")



# dashboard view 
@login_required(login_url='my-login')
def dashboard(request):
    my_record=Record.objects.all()

    context = {'records':my_record}
    return render (request,'Student/dashboard.html',context)



# create a Record
@login_required(login_url="my-login")
def create_record(request):
    form = AddRecordForm()
    if request.method=='POST':

        form =AddRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Record created succesfully")

        return redirect ('dashboard')

    context = {'form':form}

    return render (request, 'Student/create-record.html',context=context)

@login_required(login_url="my-login")
def Update_Record(request,pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method=="POST":
        form = UpdateRecordForm(request.POST,instance=record)

        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated succesfully")

        return redirect("dashboard")

    context = {"form":form}

    return render (request,'Student/update-record.html', context=context)



# view function
@login_required(login_url='my-login')
def view_record(request,pk):
    all_record = Record.objects.get(id=pk)

    context={'record':all_record}

    return render(request, 'Student/view-record.html',context=context)



# delete record

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request,'Record was deleted')

    return redirect ("dashboard")