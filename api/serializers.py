from rest_framework import serializers
from core.models import Question, Answer
from users.models import User

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    answers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            "title",
            "body",
            "author",
            "created",
            "edited",
            "answers",
        ]

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    question = serializers.ReadOnlyField(source="question.title")
    class Meta:
        model = Answer
        fields = [
            "question",
            "body",
            "author",
            "created",
        ]
