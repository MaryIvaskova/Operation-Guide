from django.contrib import admin
from .models import App, Instruction, Step, Feedback
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.utils.safestring import mark_safe


class StepInlineForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Step
        fields = '__all__'


class StepInline(admin.StackedInline):
    model = Step
    form = StepInlineForm
    extra = 1
    ordering = ['order']
    readonly_fields = ['preview_image']

    def preview_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;" />')
        return "(немає зображення)"
    preview_image.short_description = "Попередній перегляд"


class InstructionAdmin(admin.ModelAdmin):
    list_display = ['title', 'app', 'category', 'created_at', 'views']
    list_filter = ['app', 'category', 'created_at']
    search_fields = ['title', 'description']
    inlines = [StepInline]

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser and 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


class AppAdmin(admin.ModelAdmin):
    list_display = ['name', 'os']
    list_filter = ['os']
    search_fields = ['name']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'instruction', 'created_at', 'is_moderated']
    list_filter = ['is_moderated', 'created_at']
    search_fields = ['text']
    readonly_fields = ['text', 'instruction', 'created_at']


admin.site.register(App, AppAdmin)
admin.site.register(Instruction, InstructionAdmin)
admin.site.register(Feedback, FeedbackAdmin)