from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import spacy.en
nlp = spacy.en.English()

class LintView(TemplateView):
    def get(self, request, **kwargs):
        text = request.GET.urlencode().decode('utf-8').replace('_', ' ')
        doc = nlp(text)
        return JsonResponse(doc[0].dep_, safe=False)
