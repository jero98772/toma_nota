from django.contrib import admin
from .models import *
"""
class personaAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")
class gusto_disgustoAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")
class decifrarmeAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")
class confianzaAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")
class actividadesAdmin(admin.ModelAdmin):
	readonly_fields=("created","updated")
admin.site.register(persona,personaAdmin)
admin.site.register(gusto_disgusto,gusto_disgustoAdmin)
admin.site.register(confianza,confianzaAdmin)
admin.site.register(decifrarme,decifrarmeAdmin)
admin.site.register(actividades,actividadesAdmin)
"""
admin.site.register(persona)
admin.site.register(gusto_disgusto)
admin.site.register(confianza)
admin.site.register(decifrarme)
admin.site.register(actividades)