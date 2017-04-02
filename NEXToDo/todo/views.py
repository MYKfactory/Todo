from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import TemplateView
from datetime import datetime
from django.http import HttpResponse
from .models import Person, Category, ResistedTodo

def index(request):
    latest_person_list = Person.objects.all()
    latest_category_list = Category.objects.all()
    latest_todo_list = ResistedTodo.objects.all()
#    t = loader.get_template('person/index.html')
#    c = Context({
#        'latest_poll_list': latest_poll_list,
#    })
    return render_to_response('summary/index.html',
                              {'latest_person_list': latest_person_list,'latest_category_list': latest_category_list,'latest_todo_list': latest_todo_list})

def tab(request):
    return render_to_response('summary/tab.html')

def easy_todo_resist(request):
    return render_to_response('summary/todo_resist.html')

def todo_today(request):
    return render_to_response('todo/today.html')

def todo_week(request):
    return render_to_response('todo/week.html')

def todo_priority(request):
    latest_priority_list = ResistedTodo.objects.all()
    return render_to_response('todo/priority.html', {'latest_priority_list': latest_priority_list})

def todo_all_list(request):
    todo_all_list = ResistedTodo.objects.all()
    return render_to_response('todo/all_list.html', {'all_list': todo_all_list})

def category_detail(request):
    latest_category_list = Category.objects.all()
    return render_to_response('category/detail.html', {'latest_category_list': latest_category_list})

def person_detail(request):
    latest_person_list = Person.objects.all()
    return render_to_response('person/detail.html', {'latest_person_list': latest_person_list})

def todo_detail(request, question_id):
    todo_list = get_object_or_404(ResistedTodo, pk=question_id)
    return render_to_response('todo/detail.html', {'todo': todo})

def results(request, question_id):
    response = "You've looiking at rth resuluts of question %s."
    return HttpResponse(response % question_id)
