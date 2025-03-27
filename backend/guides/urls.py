from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    InstructionListAPIView,
    InstructionDetailAPIView,
    AppListAPIView,
    FeedbackCreateAPIView,
    ReviewViewSet,
)

# Створюємо router для ViewSet
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')

# Основні URL-шляхи
urlpatterns = [
    path('instructions/', InstructionListAPIView.as_view(), name='instruction-list'),
    path('instructions/<int:pk>/', InstructionDetailAPIView.as_view(), name='instruction-detail'),
    path('apps/', AppListAPIView.as_view(), name='app-list'),
    path('feedback/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
]

# Додаємо маршрути router-а до urlpatterns
urlpatterns += router.urls