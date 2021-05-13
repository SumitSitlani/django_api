from django.db import models

class Register(models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=80)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    mobile=models.CharField(max_length=12)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=80)
