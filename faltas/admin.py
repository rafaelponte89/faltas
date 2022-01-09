from django.contrib import admin
from .models import Anos, Cargos, Disciplinas,Professores, Afastamentos, Jornadas, \
        AfastamentosProfessores,ProfessoresAulas
# Register your models here.
admin.site.register(Anos)
admin.site.register(Cargos)
admin.site.register(Disciplinas)
admin.site.register(Professores)
admin.site.register(Afastamentos)
admin.site.register(Jornadas)
admin.site.register(AfastamentosProfessores)
admin.site.register(ProfessoresAulas)

