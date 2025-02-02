from rest_framework import generics
from .serializers import FAQSerializer
from .models import FAQ

# Create your views here.
class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        queryset = FAQ.objects.all()
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
        return queryset