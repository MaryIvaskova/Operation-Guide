from rest_framework import generics, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Instruction, App, Feedback, Review
from .serializers import (
    InstructionSerializer,
    AppSerializer,
    FeedbackSerializer,
    ReviewSerializer
)


# 🧠 Список інструкцій з фільтрацією, пошуком, сортуванням
class InstructionListAPIView(generics.ListAPIView):
    queryset = Instruction.objects.prefetch_related('steps').select_related('app')
    serializer_class = InstructionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['app__name', 'category', 'app__os']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'views']


# 📌 Деталі однієї інструкції
class InstructionDetailAPIView(generics.RetrieveAPIView):
    queryset = Instruction.objects.prefetch_related('steps').select_related('app')
    serializer_class = InstructionSerializer


# 📱 Список застосунків
class AppListAPIView(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


# 💬 Додати фідбек
class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


# 🌟 CRUD для Review з фільтрацією, сортуванням, безпекою
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['instruction']
    ordering_fields = ['created_at', 'rating']