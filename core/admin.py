from django.contrib import admin
from .models import Application, Instruction
from django.utils.safestring import mark_safe

class InstructionAdmin(admin.ModelAdmin):
    list_display = ('title', 'app', 'created_at')
    search_fields = ('title', 'app__name')
    list_filter = ('app', 'created_at')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['steps'].widget.attrs['style'] = 'height: 400px;'  # Увеличиваем размер редактора
        return form

admin.site.register(Application)
admin.site.register(Instruction, InstructionAdmin)