"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as core_views
from api import views as api_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("registration.backends.simple.urls")),
    path('', core_views.ListQuestions.as_view(), name="list_questions"),
    path('question/add', core_views.AddQuestion.as_view(), name="add_question"),
    path('question/<int:pk>', core_views.ShowQuestion.as_view(), name="show_question"),
    path('question/<int:pk>/add_answer', core_views.AddAnswer.as_view(), name="add_answer"),
    path('answer/<int:pk>/delete', core_views.DeleteAnswer.as_view(), name="delete_answer"),
    path('question/<int:pk>/delete', core_views.DeleteQuestion.as_view(), name="delete_question"),
    path('user/<int:pk>', core_views.UserProfile.as_view(), name="user_profile"),
    path('question/<int:pk>/fave', core_views.ToggleFavoriteQuestion.as_view(), name="toggle_question_fave"),
    path('answer/<int:pk>/fave', core_views.ToggleFavoriteAnswer.as_view(), name="toggle_answer_fave"),
    path('answer/<int:pk>/correct', core_views.ToggleCorrectAnswer.as_view(), name="toggle_answer_correct"),
    path('questions/search_results', core_views.SearchQuestions.as_view(), name="search"),
    path('question/<int:pk>/edit', core_views.EditQuestion.as_view(), name="edit_question"),
    path('answer/<int:pk>/edit', core_views.EditAnswer.as_view(), name="edit_answer"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/questions', api_views.QuestionList.as_view(), name="api_question_list"),
    path('api/questions/<int:pk>', api_views.QuestionDetail.as_view(), name="api_question_detail"),
    path('api/answers', api_views.AnswerList.as_view(), name="api_answer_list"),
    path('api/answers/<int:pk>', api_views.AnswerDetail.as_view(), name="api_answer_detail"),
    path('api/questions/<int:q_pk>/answers', api_views.QuestionAnswerList.as_view(), name="api_qa_list"),
    path('api/', api_views.api_root),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
