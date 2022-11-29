from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, ImageForm
from django.contrib.auth import authenticate, login, logout
from .models import Image

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'app/home.html', {'images': images})

def uploadImage(request):
    if request.user.is_authenticated:
        user = request.user
        
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            
            if form.is_valid():
                image = form.save(commit=False)
                image.user = user
                image.save()
                return redirect('home')
        else:
            form = ImageForm()

        return render(request, 'app/upload.html', {'form': form})

def delete_image(request, id):
        image = Image.objects.get(id=id)
        image.delete()
        return redirect('home')

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = SignUpForm()
            
        return render(request, 'account/user_signup.html', {'form': form})

    else:  
        return redirect('home')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = LoginForm()

        return render(request, 'account/user_login.html', {'form': form})
    
    else:
        return redirect('home')
    
def user_logout(request):
    logout(request)
    return redirect('login')
    
            
        