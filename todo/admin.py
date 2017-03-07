from django.contrib import admin

from .models import ResistedTodo
from .models import Person
from .models import Category
'''
class ResistedTodoAdmin(admin.ModelAdmin):
    fields = ['todo_name',
                'category',
                'cleared',
                'person',
                'memo',
                'relational_file']
'''

class ResistedTodoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['todo_name']}),
        ('memo data',{'fields':['category','memo','person','cleared','relational_file']}),
    ]
    list_filter = ['pub_date']
    date_hierarchy = 'todo_name'
    date_hierarchy = 'pub_date'

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(ResistedTodo,ResistedTodoAdmin)
#admin.site.register(ResistedTodo)
