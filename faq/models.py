from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    def __str__(self):
        return self.question
    
