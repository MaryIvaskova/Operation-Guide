from django.contrib import admin
from django.urls import path
from operation_guide.views import home, app_list, instruction_list, instruction_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('apps/', app_list, name='app_list'),
    path('apps/<int:app_id>/instructions/', instruction_list, name='instruction_list'),
    path('instructions/<int:instruction_id>/', instruction_detail, name='instruction_detail'),
]