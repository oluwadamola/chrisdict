from django.shortcuts import render
from pydictionary import Dictionary

# Create your views here.


def search(request):
    if not request.GET.get('search'):
        word = request.GET.get('search')
        dict = Dictionary(word)
        meanings = dict.meanings()
        synonyms = dict.synonyms()
        antonyms = dict.antonyms()

        context = {
            'meanings': meanings,
            'synonyms': synonyms,
            'antonyms': antonyms
        }

        return render(request, 'result.html', context)
    else:
        return render(request, 'result.html')
