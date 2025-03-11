from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from core.models import Instruction

def download_instruction_pdf(request, instruction_id):
    instruction = Instruction.objects.get(id=instruction_id)
    html_string = render_to_string('pdf_template.html', {'instruction': instruction})
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{instruction.title}.pdf"'
    return response