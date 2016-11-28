from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import spacy.en
nlp = spacy.en.English()

class LintView(TemplateView):
    def get(self, request, **kwargs):
        try:
            text = request.GET.urlencode().decode('utf-8').replace('_', ' ')
            doc = nlp(text)
        except:
            pass
        finally:
            print doc[0].orth_
            return JsonResponse(doc[0].dep_, safe=False)
