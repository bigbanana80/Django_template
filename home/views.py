from django.views.generic import TemplateView
from datetime import datetime
# Create your views here.


class Index(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["YEAR"] = datetime.today().year
        return context
