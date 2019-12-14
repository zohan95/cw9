from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Photo, Comment


class IndexClass(ListView):
    model = Photo
    template_name = 'index.html'
    ordering = ['-date_create']


@method_decorator(ensure_csrf_cookie, name='dispatch')
class DetailedView(DetailView):
    model = Photo
    template_name = 'detailed.html'
    context_object_name = 'objecto'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        curr_image = Photo.objects.get(pk=self.kwargs.get('pk'))
        comments = Comment.objects.filter(photo=curr_image)
        context['comments'] = comments
        return context


class ChangeView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    permission_required = 'webapp.change_photo'
    model = Photo
    template_name = 'update.html'
    fields = ['photo', 'sign']
    success_url = reverse_lazy('index_url')


class PhotoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_photo'
    model = Photo
    template_name = 'delete.html'
    success_url = reverse_lazy('index_url')


class PhotoCreateView(LoginRequiredMixin,CreateView):
    model = Photo
    template_name = 'create.html'
    fields = ['photo', 'sign']
    success_url = reverse_lazy('index_url')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
