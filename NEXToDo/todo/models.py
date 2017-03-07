import datetime

from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class ResistedTodo(models.Model):
    todo_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    cleared = models.BooleanField()
    pub_date = models.DateTimeField(auto_now=True)
    relational_file = models.FileField(blank=True,upload_to='uploads/%Y/%m/%d/')
    memo = models.TextField(blank=True)
    def __str__(self):
        return self.todo_name
