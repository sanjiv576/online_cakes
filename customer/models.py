from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(auto_created=True, primary_key = True)
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=300, default="")
    age = models.IntegerField(max_length=123, default=0)
    image = models.FileField(upload_to="static/images/customer", default="default.jpg")




    class Meta:
        db_table = "customer"