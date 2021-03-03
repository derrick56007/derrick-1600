import os
import json
import spacy
import stanza
from bottle import route, run, request, template

nlp_spacy = spacy.load("en_core_web_sm") # load spaCy model
nlp_stanza = stanza.Pipeline('en') # initialize English neural pipeline

@route('/ner')
def ner_api():
    """ Runs NER on any given text. The data must be sent as json and contain 'text' and 'option'.
        'option' must be one of ['spaCy', 'Stanza']
     """

    # get text and nlp option from request
    text = request.json['text']
    option = request.json['option']

    # will store the entities
    ents = []

    # use stanza nlp
    if option == 'Stanza':
        doc = nlp_stanza(text) # run annotation over a sentence
        for ent in doc.entities:
            ents.append([ent.text, ent.start_char, ent.end_char, ent.type])

    # use spacy nlp as default
    else:
        doc = nlp_spacy(text) # run annotation over a sentence
        for ent in doc.ents:
            ents.append([ent.text, ent.start_char, ent.end_char, ent.label_])

    # create response
    response = {
        'text': text,
        'ents': ents,
        'option': option,
    }

    # return response as json
    return json.dumps(response)

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8081))

    run(host=host, port=port, debug=True)

