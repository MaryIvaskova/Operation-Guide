from django.urls import path
from .views import InstructionListAPIView, InstructionDetailAPIView, AppListAPIView, FeedbackCreateAPIView

urlpatterns = [
    path('instructions/', InstructionListAPIView.as_view(), name='instruction-list'),
    path('instructions/<int:pk>/', InstructionDetailAPIView.as_view(), name='instruction-detail'),
    path('apps/', AppListAPIView.as_view(), name='app-list'),
    path('feedback/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
]