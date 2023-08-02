from django.urls import path
from aasha import views

app_name= 'aasha'
urlpatterns = [
     path('about', views.about, name='about'),
     path('contact', views.contact, name='contact'),
     path('course_details', views.course_details, name='course_details'),
     path('courses', views.courses, name='courses'), 
     path('events', views.events, name='events'), 
     path('index', views.index, name='index'),
     path('pricing', views.pricing, name='pricing'),
     path('trainers', views.trainers, name='trainers'),
]

