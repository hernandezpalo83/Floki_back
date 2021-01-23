"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view

from sgp.views import EstadoViewSet, SprintViewSet, ProyectoViewSet, EmpresaViewSet, Tipo_tareaViewSet, TareaViewSet, AsignadoViewSet, ObservadorViewSet, ComentarioViewSet, SubtareaViewSet

schema_view = get_swagger_view(title='Pastebin API')



router = routers.DefaultRouter()
router.register(r'Estado', EstadoViewSet)
router.register(r'Sprint', SprintViewSet)
router.register(r'Proyecto', ProyectoViewSet)
router.register(r'Empresa', EmpresaViewSet)
router.register(r'TipoTarea', Tipo_tareaViewSet)
router.register(r'Tarea', TareaViewSet)

router.register(r'Asignado', AsignadoViewSet)
router.register(r'Observador', ObservadorViewSet)
router.register(r'Comentario', ComentarioViewSet)
router.register(r'Subtarea', SubtareaViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'doc/', schema_view),
    url(r'^', include(router.urls)),

]
