from django.contrib import admin

from .models import ResistedTodo
from .models import Person
from .models import Category

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(ResistedTodo)
