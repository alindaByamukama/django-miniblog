from django.shortcuts import render
from django.contrib.auth.forms import RegisterUserForm

# Create your views here.
def register_user(request):
    # if request.method == 'POST':
    form = RegisterUserForm()
        
    return render(request, 'users/register_user.html', {"form": form})