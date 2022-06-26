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


def edit(request, c_id):
    print(c_id)
# id is from model and c_id from urls.py of customer
    data = Customer.objects.get(id=c_id)

    return render(request, "customer/edit.html", {'data':data})


def update(request, c_id):
    data = Customer.objects.get(id=c_id)
    # instance specifies which row of the db to be updated
    form = CustomerForm(request.POST, request.FILES, instance=data)
    form.save()

    return redirect("/customer/showCustomer")


def delete(request, c_id):

    data = Customer.objects.get(id=c_id)
    data.delete()

    return redirect("/customer/showCustomer")
    





