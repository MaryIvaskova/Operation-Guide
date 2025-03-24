from rest_framework import generics, filters
from .models import Instruction, App, Feedback
from .serializers import InstructionSerializer, AppSerializer, FeedbackSerializer
from django_filters.rest_framework import DjangoFilterBackend


class InstructionListAPIView(generics.ListAPIView):
    queryset = Instruction.objects.prefetch_related('steps').select_related('app').all()
    serializer_class = InstructionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['app__name', 'category', 'app__os']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'views']


class InstructionDetailAPIView(generics.RetrieveAPIView):
    queryset = Instruction.objects.prefetch_related('steps').select_related('app').all()
    serializer_class = InstructionSerializer


class AppListAPIView(generics.ListAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer


class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer