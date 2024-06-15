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
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from sgp.views import EstadoViewSet, SprintViewSet, ProyectoViewSet, EmpresaViewSet, Tipo_tareaViewSet, TareaViewSet, AsignadoViewSet, ObservadorViewSet, ComentarioViewSet, SubtareaViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Floki API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register('Estado', EstadoViewSet)
router.register('Sprint', SprintViewSet)
router.register('Proyecto', ProyectoViewSet)
router.register('Empresa', EmpresaViewSet)
router.register('TipoTarea', Tipo_tareaViewSet)
router.register('Tarea', TareaViewSet)

router.register('Asignado', AsignadoViewSet)
router.register('Observador', ObservadorViewSet)
router.register('Comentario', ComentarioViewSet)
router.register('Subtarea', SubtareaViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('/', include(router.urls)),

]
