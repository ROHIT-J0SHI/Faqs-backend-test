from django.test import TestCase
from django.urls import reverse
from .models import FAQ

class FAQTests(TestCase):
    def setUp(self):
        """Set up test data before each test."""
        self.faq1 = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python web framework."
        )
        self.faq2 = FAQ.objects.create(
            question="How do I install Django?",
            answer="You can install Django using pip: `pip install django`."
        )
        self.faq3 = FAQ.objects.create(
            question="Is Django good for beginners?",
            answer="Yes, Django is beginner-friendly and well-documented."
        )

    def test_faq_model(self):
        """Test FAQ model data creation."""
        faqs = FAQ.objects.all()
        self.assertEqual(faqs.count(), 3)

        self.assertEqual(self.faq1.question, "What is Django?")
        self.assertEqual(self.faq1.answer, "Django is a Python web framework.")

        self.assertEqual(self.faq2.question, "How do I install Django?")
        self.assertEqual(self.faq2.answer, "You can install Django using pip: `pip install django`.")

        self.assertEqual(self.faq3.question, "Is Django good for beginners?")
        self.assertEqual(self.faq3.answer, "Yes, Django is beginner-friendly and well-documented.")

    def test_api_returns_all_faqs(self):
        """Test API returns all FAQs in the default language."""
        response = self.client.get(reverse('faq_list'))  # Fetch FAQs
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["total_faqs"], 3) 
        self.assertEqual(len(data["faqs"]), 3) 

    def test_api_language_translation(self):
        """Test API returns FAQs in a different language (Hindi)."""
        response = self.client.get(reverse('faq_list') + "?lang=hi")  
        self.assertEqual(response.status_code, 200)

        data = response.json()

        
        self.assertEqual(data["status"], "success")  
        self.assertIn("total_faqs", data)
        self.assertIn("faqs", data)  
        self.assertTrue(isinstance(data["faqs"], list))  
        if data["faqs"]:  
            self.assertIn("question", data["faqs"][0])
            self.assertIn("answer", data["faqs"][0])
