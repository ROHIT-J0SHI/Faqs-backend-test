from django.db import models
from django.utils.translation import gettext_lazy as _
from googletrans import Translator

translator = Translator()

LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
}

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = models.TextField(_("Answer"))

    question_hi = models.TextField(_("Question in Hindi"), blank=True, null=True)
    question_bn = models.TextField(_("Question in Bengali"), blank=True, null=True)
    answer_hi = models.TextField(_("Answer in Hindi"), blank=True, null=True)
    answer_bn = models.TextField(_("Answer in Bengali"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text

        super().save(*args, **kwargs)

    def get_translation(self, lang='en'):
        if lang == 'hi':
            return {'question': self.question_hi, 'answer': self.answer_hi}
        elif lang == 'bn':
            return {'question': self.question_bn, 'answer': self.answer_bn}
        return {'question': self.question, 'answer': self.answer}

    def __str__(self):
        return self.question
