from django.urls import path 
from . import views
urlpatterns = [
    path('', views.quizlist, name='quizlist'),
]
