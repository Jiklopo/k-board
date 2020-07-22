from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Add, UserInfo
from main.forms import AddForm


class AddsListView(generic.ListView):
    template_name = 'adds/adds.html'
    model = Add
    paginate_by = 20
    ordering = '-created'


class AddDetailView(generic.DetailView):
    template_name = 'adds/add.html'
    model = Add


class AddFormView(LoginRequiredMixin, FormView):
    template_name = 'adds/form.html'
    form_class = AddForm

    def form_valid(self, form):
        add = Add(user_id=self.request.user.id, **form.cleaned_data)
        add.save()
        self.success_url = reverse('main:add_detail', args=[add.id])
        return super().form_valid(form)


class AddUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'adds/form.html'
    model = Add
    form_class = AddForm

    def form_valid(self, form):
        add = form.instance
        add.title = form.cleaned_data['title']
        add.description = form.cleaned_data['description']
        add.save()
        self.success_url = reverse('main:add_detail', args=[add.id])
        return super().form_valid(form)


class AddDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Add

    def get_success_url(self):
        return self.request.GET.get('next') or reverse('main:profile')
