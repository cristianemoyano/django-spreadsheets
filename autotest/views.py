from autotest.models import Responses, Autotest
from django.views.generic.list import ListView


class ResponseListView(ListView):

    model = Responses
    paginate_by = 10

    def get_queryset(self):
        dni_val = self.request.GET.get('dni', '')
        new_context = Responses.objects.filter(dni=None)
        if dni_val:
            new_context = Responses.objects.filter(
                dni=dni_val,
            )
        return new_context

    def get_context_data(self, **kwargs):
        context = super(ResponseListView, self).get_context_data(**kwargs)
        context['dni'] = self.request.GET.get('dni', '')
        autotest = Autotest.objects.all()
        if autotest:
            context['autotest'] = autotest[0]
        else:
            context['autotest'] = None
        return context
