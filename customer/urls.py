

from customer import views
from django.urls import path


urlpatterns = [
    path("/create", views.createForm),
    path("/save", views.saveData),
    path("/showCustomer", views.showCustomer),
    path("/edit/<int:c_id>", views.edit),
    path("/update/<int:c_id>", views.update),
    path("/delete/<int:c_id>", views.delete),
]

