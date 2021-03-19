from django.db import models
from django.utils import timezone

class NoteBook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True, blank=True)
    plain_note = models.TextField(blank=True)
    update_date = models.DateTimeField('date Updated', default=timezone.now())
    def __str__ (self):
        return "{}".format(self.title)
