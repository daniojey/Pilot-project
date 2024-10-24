# tests/urls.py

from django.urls import path
from tests import views

app_name = "tests"

urlpatterns = [
    path('', views.index, name="index"),
    path("rating/", views.UserRatingView.as_view(), name="rating"),
    path("rating/<int:test_id>", views.RatingTestView.as_view(), name="rating_test"),
    path('all_tests/', views.AllTestsView.as_view() , name='all_tests'),
    path('test/<int:test_id>', views.TestPreviewView.as_view() , name='test_preview'),
    path('create/', views.CreateTestView.as_view(), name='create_test'),
    path('delete/<int:test_id>', views.delete_test, name='delete_test'),
    path('add_question_group/<int:test_id>/', views.AddQuestionGroupView.as_view(), name='add_question_group'),
    path('<int:test_id>/add_questions/', views.AddQuestionsView.as_view(), name='add_questions'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('<int:question_id>/add_answers/', views.AddAnswersView.as_view(), name='add_answers'),
    path('<int:answer_id>/delete_answer/', views.delete_answer, name='delete_answer'),
    path('<int:question_id>/add_matching_pair/', views.AddMathicngPairView.as_view(), name='add_matching_pair'),
    path('<int:test_id>/complete_questions/', views.complete_questions, name='complete_questions'),
    path('tests_group_reviews/<int:test_id>/', views.TestGroupReviewsView.as_view(), name='test_group_reviews'),
    path('test_st/<int:test_id>/', views.TakeTestView.as_view(), name='take_test'),
    path('results/<int:test_id>/', views.TestsResultsView.as_view(), name='test_results'),
    path('tests_for_review/', views.TestsForReviewView.as_view(), name='tests_for_review'),
    path('tests_for_review/<int:user_id>/<int:test_id>/', views.take_test_review, name='take_test_review'),
    path('success_page/', views.success_manual_test, name='success_page'),
]
