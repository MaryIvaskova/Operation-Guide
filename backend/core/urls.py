from django.urls import path
from .views import InstructionListView

urlpatterns = [
    path('instructions/', InstructionListView.as_view(), name='instruction-list'),
]