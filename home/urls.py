
from home import views
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("aboutUs/", views.aboutUs, name="about"),
    path("school/", views.school, name="school"),
    
    ]