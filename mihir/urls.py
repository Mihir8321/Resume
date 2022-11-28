from django.contrib import admin
from django.urls import path,include
from mihir import views

urlpatterns = [
    path('',views.intro,name='home'),
    path('education',views.education,name='education'),
    path('work',views.work,name='work'),
    path('awards',views.awards,name='awards'),
    path('contact',views.contact,name='contact'),
    path('projects',views.projects,name='projects'),
    path('skills',views.skills,name='skills'),
    path('intro',views.intro,name='resume'),
]