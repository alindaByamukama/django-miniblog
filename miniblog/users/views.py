from django.shortcuts import render
from django.contrib.auth.form import RegisterUserForm

# Create your views here.
def register_user(request):
    # if request.method == 'POST':
    #     form = RegisterUser(request.POST)
        
    return render(request, 'users/register_user.html')