from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()        
    return render(request, 'users/register_user.html', {"form": form})

def login_user(request):
    if request.method == "POST":
        return redirect("users:login")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})