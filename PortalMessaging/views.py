from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from PortalMessaging.models import Message


class IndexMessage(ListView):
    template_name = 'Message/index.html'
    model = Message

    def get_queryset(self):
        queryset = Message.objects.filter(receiver=self.request.user)
        return queryset




class MessageDetails(TemplateView):
    template_name = "Message/details.html"
    model = Message

    def get(self, request, *args, **kwargs):
        message = get_object_or_404(Message, id=kwargs['message_id'])
        if self.request.user == message.receiver or self.request.user == message.sender:
            print(self.request.user.userprofile)
            context = self.get_context_data(**kwargs)
            print kwargs, args, request
            context['message'] = message
            return self.render_to_response(context)
        else:
            raise PermissionDenied
