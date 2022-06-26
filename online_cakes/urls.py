
# from django.contrib import admin

from home import views
from customer import views

from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include("home.urls")),  # routing if in case path is empty --> home/views.py  views.index
    path("aboutUs", include("home.urls")),
    path("school", include("home.urls")),
    path("customer", include("customer.urls")),
]


