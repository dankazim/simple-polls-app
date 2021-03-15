from django.db import models

class NoteBook(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    plain_note = models.TextField(blank=True)
    
    def __str__ (self):
        return "{} ".format(self.title)
