from django.shortcuts import redirect
from django.urls import reverse_lazy

from webapp.forms import PollForm
from webapp.models import Poll

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = Poll
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    ordering = ['-created_at']
    paginate_by = 5


class PollView(DetailView):
    model = Poll
    template_name = 'polls/poll_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices'] = self.object.choices.all()
        return context


class CreatePoll(CreateView):
    form_class = PollForm
    template_name = 'polls/create.html'

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.save()
        form.save()
        return redirect('poll_view', pk=poll.pk)


class UpdatePoll(UpdateView):
    form_class = PollForm
    template_name = 'polls/update.html'
    model = Poll


class DeletePoll(DeleteView):
    model = Poll
    template_name = 'polls/delete.html'
    success_url = reverse_lazy('index')
