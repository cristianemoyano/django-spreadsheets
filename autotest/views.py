from autotest.models import Responses, Autotest
from django.views.generic.list import ListView


class ResponseListView(ListView):

    model = Responses
    paginate_by = 10

    def get_queryset(self):
        dni_val = self.request.GET.get('dni', '')
        name_val = self.request.GET.get('name', '')
        if dni_val or name_val:
            new_context = Responses.objects.filter(
                dni__contains=dni_val,
                nombre_completo__contains=name_val,
            )
        else:
            new_context = Responses.objects.all()
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ResponseListView, self).get_context_data(**kwargs)
        context['dni'] = self.request.GET.get('dni', '')
        context['name'] = self.request.GET.get('name', '')
        context['autotest'] = Autotest.objects.all()[0]
        return context
