from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
def create_note(request):
    title = request.POST['title']
    content = request.POST['content']
   # note = Note(title=title, content=content, doc=timezone.now())
    #note.save()
    return HttpResponseRedirect(reverse('note_keeper:index'))