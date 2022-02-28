from django.urls import path
#from django.urls.resolvers import URLPattern
from FirstApp import views
urlpatterns = [
path("", views.home, name="home"), 
path("Greet/", views.greeting, name="Greet"),
path("Ashank", views.ashank, name="Ashank"),
path('Hi/', views.hellothere, name='Hello'),
path('Hello/<name>',views.hellothere1, name = 'Hi'),
path('Calc',views.calc,name = 'calc'),
path('Style', views.style,name = 'Style'),
path("Webpage", views.website1, name = "Web"),
path("pm/", views.pm, name = "pm"),
path("vm/", views.vm, name = "vm"),
path("robotics/", views.robotics, name = 'robotics'),
path("hostel/", views.hostel, name = 'hostel'),
path('script/', views.scripting, name = 'Python_Script'),
path('getpdf/', views.getpdf, name = 'gotpdf'),
path('upload/', views.upload, name = 'upload'),
path('databaseform/', views.showform, name = 'sqlitedb1'),
path('displayform/',  views.display, name = 'sqlitedbsqlite'),

]

