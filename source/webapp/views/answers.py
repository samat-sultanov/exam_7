from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView

from webapp.models import Answer, Poll, Choice


class AnswerCreateView(CreateView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        poll = get_object_or_404(Poll, pk=pk)
        context = {"poll": poll}
        return render(request, "answers/answers_view.html", context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        poll = get_object_or_404(Poll, pk=pk)
        choice_pk = request.POST.get("choice")
        print(choice_pk)
        choice = get_object_or_404(Choice, pk=choice_pk)
        Answer.objects.create(poll=poll, option=choice)
        return redirect("index")
