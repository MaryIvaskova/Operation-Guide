from django.contrib import admin
from .models import Device, App, Instruction, InstructionStep, Feedback, Shortcut, SupportLink, AdBlock, CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Права доступу", {"fields": ("role", "is_staff", "is_superuser")}),
    )
    ordering = ("email",)
    search_fields = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Device)
admin.site.register(App)
admin.site.register(Instruction)
admin.site.register(InstructionStep)
admin.site.register(Feedback)
admin.site.register(Shortcut)
admin.site.register(SupportLink)
admin.site.register(AdBlock)