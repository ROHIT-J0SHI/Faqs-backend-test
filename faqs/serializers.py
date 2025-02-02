from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'answer']

    def get_translated_question(self, obj):
        """Retrieve the translated question dynamically based on the request language."""
        request = self.context.get('request')
        lang = request.query_params.get('lang', 'en') if request else 'en'
        return obj.get_translated_question(lang)
