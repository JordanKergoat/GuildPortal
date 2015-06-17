from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView
from PortalMessaging.forms import MessageForm, ReplyForm
from PortalMessaging.models import Message

class ReplyView(FormView):
    template_name = 'Message/write_msg.html'
    form_class = ReplyForm
    success_url = reverse_lazy('message_index')

    def get_initial(self):
        initial = super(ReplyView, self).get_initial()
        initial['sender'] = self.request.user
        message = get_object_or_404(Message, id=self.kwargs['message_id'])
        initial['receiver'] = message.sender
        initial['topic'] = "RE : " + message.topic
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        message = get_object_or_404(Message, id=self.kwargs['message_id'])
        self.object.receiver = message.sender
        self.object.save()
        return super(ReplyView, self).form_valid(form)


class MessageView(FormView):
    template_name = 'Message/write_msg.html'
    form_class = MessageForm
    success_url = reverse_lazy('message_index')

    def get_initial(self):
        initial = super(MessageView, self).get_initial()
        initial['sender'] = self.request.user
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        self.object.save()
        return super(MessageView, self).form_valid(form)



class IndexMessage(ListView):
    template_name = 'Message/index.html'
    model = Message

    def get_queryset(self):
        queryset = Message.objects.filter(receiver=self.request.user).order_by('-time_send')
        return queryset



class MessageDetails(TemplateView):
    template_name = "Message/details.html"
    model = Message

    def get(self, request, *args, **kwargs):
        message = get_object_or_404(Message, id=kwargs['message_id'])
        if self.request.user == message.receiver or self.request.user == message.sender:
            context = self.get_context_data(**kwargs)
            context['message'] = message
            return self.render_to_response(context)
        else:
            raise PermissionDenied
