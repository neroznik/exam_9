from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView

from webapp.models import Picture
from webapp.forms import PictureForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


class IndexView(ListView):
    template_name = 'picture/index.html'
    context_object_name = 'picture'
    paginate_by = 5
    paginate_orphans = 0
    model = Picture
    ordering = ['-uploaded']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PictureView(TemplateView):
    template_name = 'picture/picture_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        picture = get_object_or_404(Picture, pk=pk)
        context['picture'] = picture
        return context



class PictureCreateView(LoginRequiredMixin, CreateView):
    template_name = 'picture/picture_create.html'
    form_class = PictureForm

    def form_valid(self, form):
        picture = form.save(commit=False)
        picture.author = self.request.user
        picture.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:picture_view', kwargs={'pk': self.object.pk})


class PictureUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'picture/picture_update.html'
    model = Picture
    form_class = PictureForm
    permission_required = 'webapp.change_picture'


    def get_success_url(self):
        return reverse('webapp:picture_view', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=self.kwargs.get('pk'))
        form = self.form_class(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class PictureDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'picture/picture_delete.html'
    model = Picture
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_picture'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user