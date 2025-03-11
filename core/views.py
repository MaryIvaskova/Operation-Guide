from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class ApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    @method_decorator(cache_page(60 * 15))  # Кэш на 15 минут
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from core.models import Application, Instruction
from django.core.cache import cache

def home(request):
    # Лічильник відвідувань сайту
    visits = cache.get("site_visits", 0)
    cache.set("site_visits", visits + 1, timeout=None)

    # Отримання списку програм
    applications = Application.objects.all()
    selected_app = None
    instructions = None

    # Фільтрація інструкцій за обраною програмою
    app_id = request.GET.get("app_id")
    if app_id:
        selected_app = get_object_or_404(Application, id=app_id)
        instructions = Instruction.objects.filter(app=selected_app)

    return render(request, "home.html", {
        "applications": applications,
        "selected_app": selected_app,
        "instructions": instructions,
        "visits": visits,
    })from django.shortcuts import render, get_object_or_404
from django.db.models import F
from core.models import Application, Instruction
from django.core.cache import cache

def home(request):
    # Лічильник відвідувань сайту
    visits = cache.get("site_visits", 0)
    cache.set("site_visits", visits + 1, timeout=None)

    # Отримання списку програм
    applications = Application.objects.all()
    selected_app = None
    instructions = None

    # Фільтрація інструкцій за обраною програмою
    app_id = request.GET.get("app_id")
    if app_id:
        selected_app = get_object_or_404(Application, id=app_id)
        instructions = Instruction.objects.filter(app=selected_app)

    return render(request, "home.html", {
        "applications": applications,
        "selected_app": selected_app,
        "instructions": instructions,
        "visits": visits,
    })