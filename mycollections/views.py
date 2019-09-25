from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.db import transaction
from django.http import HttpResponse
# Create your views here.


class HomepageView(TemplateView):
    template_name = "mycollections/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.order_by('id')
        context['clientes'] = Cliente.objects.order_by('id')
        return context


##########################################################################
#                           Collection views                             #
##########################################################################

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'mycollections/collection_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        return context


class CollectionCreate(CreateView):
    model = Collection
    template_name = 'mycollections/collection_create.html'
    form_class = CollectionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CollectionCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST)
        else:
            data['titles'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mycollections:collection_detail', kwargs={'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class ClienteCreate(CreateView):
    model = Cliente
    template_name = 'mycollections/cliente_create.html'
    form_class = ClienteForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(ClienteCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['contatos'] = ContatoFormSet(self.request.POST)
        else:
            data['contatos'] = ContatoFormSet()
            data['aplicacao_proprietario_slug'] = self.kwargs['aplicacao_proprietario_slug']
            data['aplicacao_slug'] = self.kwargs['aplicacao_slug']
            data['propriedade_slug'] = self.kwargs['propriedade_slug']
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        contatos = context['contatos']
        with transaction.atomic():
#            form.instance.created_by = self.request.user
            self.object = form.save()
            if contatos.is_valid():
                contatos.instance = self.object
                contatos.save()
        return super(ClienteCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mycollections:cliente_detail', kwargs={'aplicacao_proprietario_slug': self.kwargs['aplicacao_proprietario_slug'], 'aplicacao_slug': self.kwargs['aplicacao_slug'], 'propriedade_slug': self.kwargs['propriedade_slug'], 'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'mycollections/cliente_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        context['aplicacao_proprietario_slug'] = self.kwargs['aplicacao_proprietario_slug']
        context['aplicacao_slug'] = self.kwargs['aplicacao_slug']
        context['propriedade_slug'] = self.kwargs['propriedade_slug']
        return context


class CollectionUpdate(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'mycollections/collection_create.html'

    def get_context_data(self, **kwargs):
        data = super(CollectionUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST, instance=self.object)
        else:
            data['titles'] = CollectionTitleFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mycollections:collection_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'mycollections/cliente_create.html'

    def get_context_data(self, **kwargs):
        data = super(ClienteUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['contatos'] = ContatoFormSet(self.request.POST, instance=self.object)
        else:
            data['contatos'] = ContatoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        contatos = context['contatos']
        with transaction.atomic():
#            form.instance.created_by = self.request.user
            self.object = form.save()
            if contatos.is_valid():
                contatos.instance = self.object
                contatos.save()
        return super(ClienteUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('mycollections:cliente_detail', kwargs={'aplicacao_proprietario_slug': self.kwargs['aplicacao_proprietario_slug'], 'aplicacao_slug': self.kwargs['aplicacao_slug'], 'propriedade_slug': self.kwargs['propriedade_slug'], 'pk': self.object.pk})


class CollectionDelete(DeleteView):
    model = Collection
    template_name = 'mycollections/confirm_delete.html'
    success_url = reverse_lazy('mycollections:homepage')
    

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'mycollections/confirm_delete.html'
    success_url = reverse_lazy('mycollections:homepage')