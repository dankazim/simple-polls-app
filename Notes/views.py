from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import NoteBook

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Notes/index.html'
    context_object_name = 'Notes_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return NoteBook.objects.order_by('pub_date')[:5]

# def create_note(request):
#     title = request.POST['title']
#     plain_note = request.POST['content']
#    # note = Note(title=title, content=content, doc=timezone.now())
#     #note.save()
#     return HttpResponseRedirect(reverse('note_keeper:index'))