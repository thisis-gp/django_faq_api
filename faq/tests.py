from django.test import TestCase
from .models import FAQ

# Create your tests here.
class FAQModelTest(TestCase):
    def test_translation(self):
        faq = FAQ(question="What is Django?", answer="Django is a web framework.")
        faq.save()
        self.assertEqual(faq.get_translated_question('ml'), faq.question_ml)