

from customer import views
from django.urls import path


urlpatterns = [
    path("/create", views.createForm),
    path("/save", views.saveData),
    path("/showCustomer", views.showCustomer)
]

