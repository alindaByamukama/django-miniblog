from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register_user(request):
    form = UserCreationForm()        
    return render(request, 'users/register_user.html', {"form": form})