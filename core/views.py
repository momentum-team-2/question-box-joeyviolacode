from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Answer, Question
from users.models import User

# Create your views here.
def list_questions(request):
    stuff = "1. Item 1\n1. Item 2\n1. Item 3\n\t1. Item 3a\n\t1. Item 3b"
    return render(request, 'core/index.html', {"stuff":stuff})