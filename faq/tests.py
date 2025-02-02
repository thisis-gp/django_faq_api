from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework."
        )

    def test_english_translation(self):
        self.assertEqual(self.faq.get_translated_question('en'), "What is Django?")

    def test_malayalam_translation(self):
        self.faq.question_ml = "ഡjango എന്താണ്?"
        self.faq.save()
        self.assertEqual(self.faq.get_translated_question('ml'), "ഡjango എന്താണ്?")

    def test_tamil_translation(self):
        self.faq.question_ta = "டjango என்றால் என்ன?"
        self.faq.save()
        self.assertEqual(self.faq.get_translated_question('ta'), "டjango என்றால் என்ன?")

    def test_fallback_to_english(self):
        self.assertEqual(self.faq.get_translated_question('invalid_lang'), "What is Django?")