from django.views.generic import TemplateView, ListView
from index.models import Advertisement


class IndexView(TemplateView):
    template_name = 'index.html'

class AdvertisementView(ListView):
    model = Advertisement
    template_name = 'fair.html'

class FairsView(ListView):
    model = Advertisement
    template_name = 'orders.html'