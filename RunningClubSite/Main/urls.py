from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home/', views.home, name='Home'), #Had to create a second home route for buttons
    path('about/', views.about, name='About'),
    path('news/', views.news, name='News'),
    path('records/', views.records, name='Records'),

]
