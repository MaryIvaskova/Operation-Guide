from django.contrib import admin
from .models import CustomUser, Device, App, Instruction, InstructionStep, AdBlock, SupportLink

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "role", "is_staff", "is_superuser")

admin.site.register(Device)
admin.site.register(App)
admin.site.register(Instruction)
admin.site.register(InstructionStep)
admin.site.register(AdBlock)
admin.site.register(SupportLink)