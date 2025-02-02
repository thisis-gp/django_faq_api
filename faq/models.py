from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

# Create your models here.
class FAQ(models.Model):
    question = models.TextField() # Question in English
    answer = RichTextField()        # Answer with WYSIWYG support
    question_ml = models.TextField(blank=True, null=True) # Malayalam Translation
    question_ta = models.TextField(blank=True, null=True) # Tamil Translation


    def __str__(self):
        return self.question
    
    def get_translated_question(self,lang):
        """
        Dynamically retrieve translated question based on language
        """
        if lang == "ml":
            return self.question_ml
        elif lang == "ta":
            return self.question_ta
        else:
            return self.question
        
    def translate_text(self, text, lang):
        translator = Translator()
        try:
            translation = translator.translate(text=text, dest=lang).text
            return translation
        except:
            return text
        
    def save(self, *args, **kwargs):
        if not self.question_ml:
            self.question_ml = self.translate_text(self.question,"ml")
        if not self.question_ta:
            self.question_ta = self.translate_text(self.question,"ta")
        cache.clear()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        cache.clear()
        return super().delete(*args, **kwargs)
