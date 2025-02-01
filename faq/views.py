from rest_framework import generics
from .serializers import FAQSerializer
from .models import FAQ

# Create your views here.
class FAQList(generics.ListAPIView):
    serializer_class = FAQSerializer

    def get_queryset(self):
        queryset = FAQ.objects.all()
        return queryset