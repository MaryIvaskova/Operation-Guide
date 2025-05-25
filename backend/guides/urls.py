from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    InstructionListAPIView,
    InstructionDetailAPIView,
    ProgramListAPIView,
    FeedbackCreateAPIView,
    TopicViewSet,
    ReviewViewSet,
    ProgramTopicsAPIView,
    InstructionFeedbackCreateAPIView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger конфігурація
schema_view = get_schema_view(
    openapi.Info(
        title="Operation Guide API",
        default_version='v1',
        description="Документація API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Router для ViewSet
router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'reviews', ReviewViewSet)

# URL patterns
urlpatterns = [
    path('instructions/', InstructionListAPIView.as_view(), name='instruction-list'),
    path('instructions/<int:pk>/', InstructionDetailAPIView.as_view(), name='instruction-detail'),
    path('instructions/<int:pk>/feedback/', InstructionFeedbackCreateAPIView.as_view(), name='instruction-feedback'),
    path('programs/', ProgramListAPIView.as_view()),
    path('feedback/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
    path('programs/<int:pk>/topics/', ProgramTopicsAPIView.as_view(), name='program-topics'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]