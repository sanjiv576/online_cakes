from django.shortcuts import render, redirect
from customer.forms import CustomerForm
from customer.models import Customer

# Create your views here.
def createForm(request):
    return render(request, "customer/create.html")


def saveData(request):
    print(request.FILES)
    print(request.POST)
    # mapping with database
    data = CustomerForm(request.POST, request.FILES)
    # save in db
    data.save()
    print(data)
    # return render(request, "customer/create.html")
    return redirect("/customer/showCustomer")


def showCustomer(request):
    customers = Customer.objects.all()
    return render(request, 'customer/show_info.html', {'customers': customers})




