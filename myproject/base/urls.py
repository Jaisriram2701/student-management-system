from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('about',about,name='about'),
    path('add_student',add_student,name='add_student'),
    path('update/<int:pk>',update,name='update'),
    path('delete/<int:pk>',delete,name='delete'),
    path('trash/', trash, name='trash'),
    path('restore/<int:pk>/', restore, name='restore'),
    path('permanent_delete/<int:pk>/', permanent_delete, name='permanent_delete'),
]