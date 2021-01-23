from django.contrib import admin
from .models import Estado, Sprint, Proyecto, Empresa, Tipo_tarea, Tarea, Asignado, Observador, Comentario, Subtarea
# Register your models here.
admin.site.register( Estado )
admin.site.register( Sprint )
admin.site.register( Proyecto )
admin.site.register( Empresa )
admin.site.register( Tipo_tarea )
admin.site.register( Tarea )
admin.site.register( Asignado )
admin.site.register( Observador )
admin.site.register( Comentario )
admin.site.register( Subtarea )

