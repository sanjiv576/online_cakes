from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from customer.views import showCustomer


def login_page(request):

    if(request.method == 'POST'):
        # fetching data from the view and compare with model
        # left username is the attribute of the table
        # right username is the name of the field
        user = authenticate(request,
                username=request.POST['username'],
                password = request.POST['password']
                )
        
        print(user)

        if(user is not None):
            # django_session table used to track who user is logined recently
            login(request, user)
            print("Login successfully")
            return redirect("/customer/showCustomer")
        else:
            print("Login failed. Sth went wrong")
            return redirect("/user/login")
    else:
        return render(request, "user/login.html")


def register_page(request):

    print(request.method)
    
    if(request.method == 'POST'):
        # insert data in predefined tabel i.e auth_user
        User.objects.create_user(

            # first_name is the attribute of the table
            # firstName is the name of the field
            first_name = request.POST['firstName'],
            last_name = request.POST['lastName'],
            email = request.POST['email'],
            username = request.POST['username'],
            password = request.POST['password']

        )

        print("Registered successfully")

        return redirect('/user/login')
        
    else:
        return render(request, "user/register.html")


# for logout

def logout_func(request):
    logout(request)
    print("user loged out")
    return redirect("/user/login")