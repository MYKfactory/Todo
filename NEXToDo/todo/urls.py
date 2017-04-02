from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^category/(?P<question_id>[0-9]+)/$', views.category_detail,name='category_detail'),
#    url(r'^person/(?P<question_id>[0-9]+)/$', views.person_detail,name='person_detail'),
#    url(r'^todo/(?P<question_id>[0-9]+)/$', views.todo_detail,name='todo_detail'),
    url(r'^category/', views.category_detail,name='category_detail'),
    url(r'^person/', views.person_detail,name='person_detail'),
    url(r'^summary/tab', views.tab,name='tab'),
    url(r'^summary/easy_todo_resist', views.easy_todo_resist,name='easy_todo_resist'),
    url(r'^todo/today', views.todo_today,name='todo_today'),
    url(r'^todo/week', views.todo_week,name='todo_week'),
    url(r'^todo/priority', views.todo_priority,name='todo_priority'),
    url(r'^todo/all_list', views.todo_all_list,name='todo_all_list'),
]
