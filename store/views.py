from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm
from django import forms


# Create your views here.


def update_password(request):
    if request.user.is_authenticated:
        current_user= request.user
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Password Update Successfully")
                # login(request,current_user)
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                    return redirect('update_password')
        else:
            form = ChangePasswordForm(current_user)
            return render(request,"update_password.html",{'form':form})
        
    else:
        messages.success(request,"You Must be logged in to update your password") 
        return redirect('home')

def update_user(request):
    if request.user.is_authenticated:
        current_users =User.objects.get(id = request.user.id)
        user_form = UpdateUserForm(request.POST or None , instance = current_users)
        if user_form.is_valid():
            user_form.save()

            login(request, current_users)
            messages.success(request,"User Has Been Updated Successfully...!!!!")
            return redirect('home')
        return render(request,"update_user.html",{'user_form':user_form})
    else:
        messages.success(request,"You Must Be Logged In To Access That Page...!!!!")
        return redirect('home')
    return render(request,'update_user.html',{})



def category_summary(request):
    categories = Category.objects.all()
    return render(request,'category_summary.html',{"categories":categories})


def category(request,foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name =foo)
        product = Product.objects.filter(category = category)
        return render(request,'category.html',{'products':product, 'category':category})
    except:
        messages.success(request,"This Category Doesn't Exist")
        return redirect('home')



def home(request):
    products =Product.objects.all()
    return render(request,'home.html',{'products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username , password= password)
        if  user is not None:
            login(request,user)
            messages.success(request,'Login Successfully Enjoy Your Journey....')
            return redirect('home') 
        else:
            messages.success(request,'Something Went Wrong Please Try Again ...')
            return redirect('login') 
    else:
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successfully.... Good Bye.. See You Seen.. ")
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username , password= password)
            login(request,user)
            messages.success(request,"You Have Been Registered Successfully...")
            return redirect('home')
        else:
            messages.success(request,"Something Went Wrong Please Try Again...")
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})

    

    

