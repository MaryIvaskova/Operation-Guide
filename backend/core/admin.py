from django.contrib import admin
from .models import Instruction
from ckeditor.widgets import CKEditorWidget
from django import forms

class InstructionAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Instruction
        fields = '__all__'

class InstructionAdmin(admin.ModelAdmin):
    form = InstructionAdminForm
    list_display = ('title', 'os_type', 'created_at')

admin.site.register(Instruction, InstructionAdmin)