from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Answer, Question
from users.models import User
from django.views import View

# Create your views here.
# def list_questions(request):
#     user = request.user
#     questions = user.questions.all()

#     return render(request, 'core/index.html', {"user":user, "questions":questions})

class ListQuestions(View):
    # stuff = "> Coffee. The finest organic suspension ever devised... I beat the Borg with it.\n\n> - Captain Janeway"
        
    def get(self, request):
        user = request.user
        questions = Question.objects.all()
        return render(request, 'core/index.html', {"questions":questions, "user":user})