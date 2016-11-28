from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
import spacy.en
import spell
import re
import pdb

nlp = spacy.en.English()

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
        try:
            text = request.GET.urlencode().decode('utf-8').replace('_', ' ')
            doc = nlp(text)
            for tok in doc:
                print tok.orth_, tok.pos_

            return JsonResponse(doc[0].orth_, safe=False)
        except Exception, e:
            return JsonResponse(str(e), safe=False)
