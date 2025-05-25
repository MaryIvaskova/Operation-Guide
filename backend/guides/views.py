from rest_framework import generics, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404

from .models import Instruction, Program, Feedback, Review, Topic
from .serializers import (
    InstructionSerializer,
    ProgramSerializer,
    FeedbackSerializer,
    ReviewSerializer,
    TopicSerializer
)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['id']


class InstructionListAPIView(generics.ListAPIView):
    queryset = Instruction.objects.prefetch_related('steps').select_related('program')
    serializer_class = InstructionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['program__name', 'category', 'program__os']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'views']


class InstructionDetailAPIView(generics.RetrieveAPIView):
    queryset = Instruction.objects.prefetch_related('steps').select_related('program')
    serializer_class = InstructionSerializer


class ProgramListAPIView(generics.ListAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class FeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['instruction']
    ordering_fields = ['created_at', 'rating']


class ProgramTopicsAPIView(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(program_id=self.kwargs["pk"])


class InstructionFeedbackCreateAPIView(CreateAPIView):
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        instruction = get_object_or_404(Instruction, pk=self.kwargs["pk"])
        serializer.save(instruction=instruction)