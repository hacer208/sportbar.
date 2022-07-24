from django.shortcuts import render
from django.contrib.auth.models import User


def login(request):
    print(request.user.is_anonymous)
    if request.user.is_anonymous == True:
        if request.POST:
            new_user = User(username=request.POST['username'])
            new_user.set_password(request.POST['password'])
            new_user.save()
            return render(request, 'users/login.html')
    else:
            return render(request, 'users/signin.html')

