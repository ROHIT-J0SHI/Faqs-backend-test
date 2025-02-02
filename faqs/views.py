from django.http import JsonResponse
from .models import FAQ

def faq_list(request):
    lang = request.GET.get('lang', 'en')  # Default language is English
    faqs = FAQ.objects.all()

    data = {
        "status": "success",
        "total_faqs": faqs.count(),
        "faqs": []
    }

    for faq in faqs:
        translated_text = faq.get_translation(lang)
        question = translated_text.get('question') or faq.question
        answer = translated_text.get('answer') or faq.answer

        data["faqs"].append({
            "id": faq.id,
            "question": question,
            "answer": answer,
        })

    return JsonResponse(data, safe=False, json_dumps_params={'indent': 4})
