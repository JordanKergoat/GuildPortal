__author__ = 'Alexandre Cloquet'

from Portal.models import Portal

def menu(request):
    return {'list_portal': Portal.objects.all()}