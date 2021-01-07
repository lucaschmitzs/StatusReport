from django.contrib import admin
from django.urls import path, include
from status_report_sistemas.views import ProjetosEntregasViewSet, GmudViewSet, TicketsImpactoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projetos_entregas', ProjetosEntregasViewSet, basename='ProjetosEntregas')
router.register('gmud', GmudViewSet, basename='Gmud')
router.register('tickets_impacto', TicketsImpactoViewSet, basename='TicketsImpacto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
