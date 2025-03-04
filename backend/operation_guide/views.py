from django.shortcuts import render, get_object_or_404
from .models import App, Instruction, InstructionStep

def home(request):
    return render(request, "operation_guide/home.html")

def app_list(request):
    apps = App.objects.all()
    return render(request, "operation_guide/app_list.html", {"apps": apps})

def instruction_list(request, app_id):
    app = get_object_or_404(App, id=app_id)
    instructions = Instruction.objects.filter(app=app)
    return render(request, "operation_guide/instruction_list.html", {"app": app, "instructions": instructions})

def instruction_detail(request, instruction_id):
    instruction = get_object_or_404(Instruction, id=instruction_id)
    steps = InstructionStep.objects.filter(instruction=instruction)
    return render(request, "operation_guide/instruction_detail.html", {"instruction": instruction, "steps": steps})

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Instruction
from .serializers import InstructionSerializer

@api_view(["GET"])
def api_instruction_list(request):
    instructions = Instruction.objects.all()
    serializer = InstructionSerializer(instructions, many=True)
    return Response(serializer.data)