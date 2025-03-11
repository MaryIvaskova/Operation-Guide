from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, InstructionViewSet
from django.urls import path
from .views import download_instruction_pdf

urlpatterns += [
    path('download/<int:instruction_id>/', download_instruction_pdf, name='download_pdf'),
]

router = DefaultRouter()
router.register(r'apps', ApplicationViewSet, basename='applications')

urlpatterns = [
    path('', include(router.urls)),
    path('instructions/<int:app_id>/', InstructionViewSet.as_view({'get': 'list'})),
]
from django.urls import path
from .views import home, instruction_detail

urlpatterns = [
    path("", home, name="home"),
    path("instruction/<int:instruction_id>/", instruction_detail, name="instruction_detail"),
]