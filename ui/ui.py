import os
import json
import random
import requests
import streamlit as st

def get_random_color(pastel_factor = 0.5):
    """ returns a random color """
    return [(x+pastel_factor)/(1.0+pastel_factor) for x in [random.uniform(0,1.0) for i in [1,2,3]]]

def color_distance(c1,c2):
    """ returns the distance between two colors """
    return sum([abs(x[0]-x[1]) for x in zip(c1,c2)])

def generate_new_color(existing_colors,pastel_factor = 0.5):
    """ returns a new random color with optimal distance """

    max_distance = None
    best_color = None
    for i in range(0,100):
        color = get_random_color(pastel_factor = pastel_factor)
        if not existing_colors:
            return color
        best_distance = min([color_distance(color,c) for c in existing_colors])
        if not max_distance or best_distance > max_distance:
            max_distance = best_distance
            best_color = color
    return best_color

# render header
st.markdown('<h1 style="font-size: 3em; text-align: center;">Named Entity Recognition</h>', unsafe_allow_html=True)

# render input box
text_in = st.text_input('Enter the text to be analyzed here:', 'Sundar Pichai is the CEO of Google. Barack Obama was born in Hawaii.') 

# render nlp library dropdown
option_in = st.selectbox('NLP Library', ('spaCy', 'Stanza'))

# render submit button
submit = st.button('Submit')

# only render if text is inputted
if text_in and option_in and submit:
    host = os.environ.get('API_HOST', 'server')
    port = int(os.environ.get('API_PORT', 8081))

    url = 'http://{}:{}/ner'.format(host, port)
    payload = {
        'text': text_in,
        'option': option_in
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
    }

    # render spinner
    with st.spinner('Wait for it...'):
        # call NER api
        response = requests.request('GET', url, data=json.dumps(payload), headers=headers)

    data = response.json()

    ################## do some pretty rendering... ##################
    html_string = '''
    <style>
        #out, .ent {
            display: flex;
        }
        #out {
            max-width: 730px;
            flex-wrap: wrap;
            align-items: center;        
        }
        .ent {
            margin: 5px;
            border: 1px black solid;
            border-radius: 5px;
            align-items: flex-end;
        }
        .ent > div {
            padding: 5px;
        }
        .ent-type {
            font-weight: 600;
            font-size: .75em;
        }
    '''

    # constants
    start_index = 1
    end_index = 2
    type_index = 3

    colors = []
    ent_types = set([ent[type_index] for ent in data['ents']])
    for ent_type in ent_types:
        # generate a random color for each entity type
        c = generate_new_color(colors,pastel_factor = 0.9)
        colors.append(c)

        html_string += '.{}'.format(ent_type)
        html_string += '{ background-color: '
        html_string += 'rgb({},{},{});'.format(int(c[0] * 255), int(c[1] * 255), int(c[2] * 255))
        html_string += '}'

    html_string += '''
    </style>
    <h3>Output:</h3>
    '''
    st.markdown(html_string, unsafe_allow_html=True)
    html_string = '<div id="out">'

    curr = 0

    for ent in data['ents']:
        # create html for entity types

        html_string += '<div>{}</div>'.format(data['text'][curr:ent[start_index]])
        html_string += '''
        <div class="ent {}">
            <div>{}</div>
            <div class="ent-type">{}</div>
        </div>'''.format(ent[type_index], data['text'][ent[start_index]:ent[end_index]], ent[type_index])
        curr = ent[end_index]


    html_string += '</div>'
    st.markdown(html_string, unsafe_allow_html=True)