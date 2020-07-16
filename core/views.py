from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Answer, Question
from .forms import AnswerForm, QuestionForm
from users.models import User
from django.views import View
from django.http import JsonResponse

# Create your views here.
# def list_questions(request):
#     user = request.user
#     questions = user.questions.all()

#     return render(request, 'core/index.html', {"user":user, "questions":questions})

class ListQuestions(View):
    # stuff = "Some *test* [link](#)"
        
    def get(self, request):
        user = request.user
        questions = Question.objects.order_by("-created")
        return render(request, 'core/index.html', {"questions":questions, "user":user})


class AddQuestion(View):
    def get(self, request):
        form = QuestionForm()
        user = request.user
        return render(request, 'core/add_question.html', {"form": form})

    def post(self, request):
        form = QuestionForm(data=request.POST)
        user = request.user
        if form.is_valid():
            question = form.save(commit=False)
            author = request.user
            question.author = author
            question.save()
        return redirect(to="list_questions")


class ShowQuestion(View):
    def get(self, request, pk):
        user = request.user
        form = AnswerForm()
        question = get_object_or_404(Question, pk=pk)
        return render(request, 'core/show_question.html', {"question": question, "user": user, "form":form})


class AddAnswer(View):
    def post(self, request, pk):
        form = AnswerForm(data=request.POST)
        user = request.user
        question = get_object_or_404(Question, pk=pk)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = user
            answer.question = question
            answer.save()
        return redirect(to="show_question", pk=pk)


class DeleteAnswer(View):
    def get(self, request, pk):
        user = request.user
        this_a_is_users = bool(Answer.objects.filter(author=user, pk=pk).count())
        if this_a_is_users:
            answer = get_object_or_404(Answer, pk=pk)
            redirect_pk = answer.question.pk
            answer.delete()
            return redirect(to='show_question', pk=redirect_pk)
        else: 
            return redirect(to='list_questions')
        


class DeleteQuestion(View): 
    def get(self, request, pk):
        user = request.user
        this_q_is_users = bool(Question.objects.filter(author=user, pk=pk).count())
        if this_q_is_users:
            question = get_object_or_404(Question, pk=pk)
            question.delete()
            return redirect(to='list_questions')
        else: 
            return redirect(to='list_questions')
        

class UserProfile(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        questions = Question.objects.filter(author=user)
        return render(request, 'core/user_profile.html', {"user":user, "questions":questions})

@method_decorator(csrf_exempt, name="dispatch")
class ToggleFavoriteAnswer(View):
    def post(self, request, pk):
        user = request.user
        answer = get_object_or_404(Answer, pk=pk)
        if answer in user.a_faves.all():
            user.a_faves.remove(answer)
            return JsonResponse({"favorite": False})
        else:
            user.a_faves.add(answer)
            return JsonResponse({"favorite": True})

@method_decorator(csrf_exempt, name="dispatch")
class ToggleFavoriteQuestion(View):

    def post(self, request, pk):
        user = request.user
        question = get_object_or_404(Question, pk=pk)
        if question in user.q_faves.all():
            user.q_faves.remove(question)
            return JsonResponse({"favorite": False})
        else:
            user.q_faves.add(question)
            return JsonResponse({"favorite": True})
