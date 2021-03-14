from django.db import models

# Create your models here.

class NoteBook(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__ (self):
    
        return "ID: {} Question text:{} Pub Date: {}".format(self.id,self.question_text,self.pub_date)
