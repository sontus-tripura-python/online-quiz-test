from django.shortcuts import render
from .models import ExamQuestion
# Create your views here.

def quizlist(request):
    resutls = ExamQuestion.objects.all()
    context = {'results': resutls}
    return render(request, 'quiz/home.html', context)