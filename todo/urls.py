from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<question_id>[0-9]+)/$', views.category_detail,name='category_detail'),
    url(r'^person/(?P<question_id>[0-9]+)/$', views.person_detail,name='person_detail'),
    url(r'^todo/(?P<question_id>[0-9]+)/$', views.todo_detail,name='todo_detail'),
]
