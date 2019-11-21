from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'), #Had to create a second home route for buttons
    path('about/', views.about, name='About'),
    url(r'^records/(?P<fullName>[\w\-]+)', views.records, name='Records'),
    path('records/', views.records, name='Records'),
    path('schedule/', views.schedule, name='Schedule'),
    path('FAQ/', views.FAQs, name='FAQ'),
    url(r'^news/(?P<year>[0-9]+)/(?P<month>[0-9]+)', views.news, name='News'),
    url(r'^news/(?P<year>[0-9]+)/', views.news, name='News'),
    path('news/', views.news, name='News'),
    path('exec/',views.Exec, name='Exec'),
    path('routes/',views.Routes, name='Routes'),
]
