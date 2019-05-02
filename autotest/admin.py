from django.contrib import admin
from autotest.models import Autotest, Responses
from autotest.domains import generate_responses_from_spreadsheets


class AutotestAdmin(admin.ModelAdmin):
    actions = ['generate_responses']

    def generate_responses(self, request, queryset):
        generate_responses_from_spreadsheets(title=queryset[0].title)
        self.message_user(request, "Respuestas cargadas exitosamente")
    generate_responses.short_description = "Generar respuestas desde Google SpreadSheets"


# Register your models here.
admin.site.register(Autotest, AutotestAdmin)
admin.site.register(Responses)
