from send_mail.settings import EMAIL_HOST_USER
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .models import RegionalUser
from .forms import RegionalUserCreateForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .filters import RegionalUserFilter
from .tables import RegionalUserTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_tables2 import SingleTableView
# Create your views here.


def home(request):
    return render(request, 'sending/home.html', {})

def correo(request):
    return render(request, 'sending/email.html', {})

class RegionalUserCreateView(CreateView):
    model = RegionalUser
    form_class = RegionalUserCreateForm
    template_name = 'sending/create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            context = {
                'name': user.name,
                'username': user.username,
                'password': user.password
            }
            sms2usr = render_to_string('sending/email.html', context)
            try:
                send_mail(
                    'Plataforma de la ENCCRV: Registro exitoso',
                    sms2usr,
                    EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False, html_message=sms2usr
                )
            except Exception as e:
                print('ERROR DEL CORREO: ', e)
            messages.success(request, '¡Usuario registrado!.')
            return redirect('home')


class RegionalUserListView(SingleTableMixin, FilterView):
    table_class = RegionalUserTable
    model = RegionalUser
    template_name = 'sending/list_copy.html'
    paginate_by = 5
    filterset_class = RegionalUserFilter
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_users'] = RegionalUser.objects.all().count()
        return context