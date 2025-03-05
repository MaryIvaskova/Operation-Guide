from rest_framework import generics
from .models import Instruction
from .serializers import InstructionSerializer

class InstructionListView(generics.ListAPIView):
    serializer_class = InstructionSerializer

    def get_queryset(self):
        os_type = self.request.GET.get('os', None)
        if os_type in ['android', 'ios']:
            return Instruction.objects.filter(os_type=os_type)
        return Instruction.objects.all()