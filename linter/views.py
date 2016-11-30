from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import spacy.en
import spell
import re

# nlp = spacy.en.English()

def words_with_indices(string):
   l = re.split("(\s|\W){1}", string)
   counter = 0
   w_i = []
   for tok in l:
       if re.match('[a-zA-Z]', tok):
           w_i.append([tok, counter])
       counter += len(tok)
   return w_i

class LintView(TemplateView):
   def get(self, request, **kwargs):
       spellings = {}
       try:
           text = request.GET.urlencode().decode('utf-8').replace('_', ' ')
        #    doc = nlp(text)
        #    for tok in doc:
        #        print tok.orth_, tok.pos_
           for word, idx in words_with_indices(text):
               correction = spell.correction(word)
               if word.lower() != correction.lower():
                   spellings[idx] = correction
           return JsonResponse(spellings)
       except Exception, e:
           return JsonResponse(str(e), safe=False)
