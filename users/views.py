from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from index.forms import CreateOrderForm
from index.models import Company, Production_categories, Advert, Advantages, Advertisement


def login_ajax(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'})

def register_ajax(request):
    print(request.POST)

@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    models = Company
    template_name = 'lk/lk-personal.html'
    context_object_name = 'company'

    def get_queryset(self):
        user = self.request.user
        return Company.objects.filter(user=user).first()

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['production_categories'] = Production_categories.objects.all()
        try:
            context['company_categories'] = Company.objects.filter(user=user).first().production_categories.all()
        except:
            pass
        return context

@method_decorator(login_required, name='dispatch')
class AdvertView(ListView):
    model = Advert
    template_name = 'lk/lk-advert.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advantages'] = Advantages.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class OrdersView(ListView):
    model = Advertisement
    template_name = 'lk/lk-orders.html'

@method_decorator(login_required, name='dispatch')
class FairsView(TemplateView):
    template_name = 'lk/lk-fairs.html'

@method_decorator(login_required, name='dispatch')
class CreateAdvertisementView(CreateView):
    model = Advertisement
    form_class = CreateOrderForm
    template_name = 'lk/lk-createOrder.html'
    success_url = '/success-url/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
