from django.db import models

# Create your models here.

class Categroy(models.Model):
    categroy_name=models.CharField(max_length=100)

class Book(models.Model):
    categroy = models.ForeignKey(Categroy,on_delete=models.CASCADE)
    book_title=models.CharField(max_length=100)


class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    father_name=models.CharField(max_length=100)