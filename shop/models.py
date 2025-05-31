from django.db import models

class Customer(models.Model):
    name      = models.CharField(max_length=100)
    birthday  = models.DateField()
    gender    = models.CharField(max_length=10)
    student_class = models.CharField(max_length=20)
    res_code  = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
