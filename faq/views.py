from rest_framework import generics
from .serializers import FAQSerializer
from .models import FAQ
from django.core.cache import cache

# Create your views here.
class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        try:
            lang = self.request.query_params.get('lang', 'en')
            cache_key = f'faqs_{lang}'
            queryset = cache.get(cache_key)
            if not queryset:
                queryset = FAQ.objects.all()
                for faq in queryset:
                    faq.question = faq.get_translated_question(lang)
                cache.set(cache_key, queryset, timeout=60*10) # Cache for 10 mins
            return queryset
        except Exception as e:
            print(e)
            return FAQ.objects.none()