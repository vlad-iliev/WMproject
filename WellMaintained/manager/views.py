from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic as views

from WellMaintained.common.decorators import allow_groups
from WellMaintained.manager.forms import ManagerCreateForm
from WellMaintained.manager.models import Manager


class ManagerCreateView(LoginRequiredMixin, views.CreateView):
    template_name = 'manager/manager-create.html'
    form_class = ManagerCreateForm
    success_url = reverse_lazy('manager list')

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args,**kwargs)


class ManagerUpdateView(LoginRequiredMixin, views.UpdateView):
    allow_groups([])
    template_name = 'manager/manager-create.html'
    form_class = ManagerCreateForm
    success_url = reverse_lazy('manager list')

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args,**kwargs)

class ManagerDetailsView(LoginRequiredMixin, views.detail.DetailView):
    allow_groups(['Directors'])
    model = Manager
    template_name = 'manager/manager-details.html'


@login_required
def managers_list_view(request):
    managers = Manager.objects.all()

    context = {
        'managers': managers,
    }

    return render(request, 'manager/manager-list.html', context)
