from django.urls import path
from django.views.generic import RedirectView

from webapp.views import IndexView, CreatePoll, PollView, UpdatePoll, DeletePoll

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('polls/', RedirectView.as_view(pattern_name='index')),
    path('polls/add/', CreatePoll.as_view(), name='create_poll'),
    path('poll/<int:pk>/', PollView.as_view(), name='poll_view'),
    path('poll/<int:pk>/update/', UpdatePoll.as_view(), name='update_poll'),
    path('poll/<int:pk>/delete/', DeletePoll.as_view(), name='delete_poll'),
]
