from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if not User.objects.filter(username=username).exists() and not User.objects.filter(email=email).exists():
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                return render(request, 'accounts\\registered.html')

            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return render(request, 'accounts\\register.html')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Account is registered with the given Email ID')
                return render(request, 'accounts\\register.html')

        elif password1 != password2:
            messages.info(request, "Passwords not matching")
            return render(request, 'accounts\\register.html')

    else:
        return render(request, "accounts\\register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'accounts\\login.html')

    else:
        return render(request, "accounts\\login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
