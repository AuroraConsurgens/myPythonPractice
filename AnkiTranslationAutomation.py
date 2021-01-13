#combination of translate + anki connect
from translate import Translator #you need to install it
import json
import urllib.request

def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

translator= Translator(from_lang="en", to_lang="ru") #you can also change translator, read translate doc

with open("workData.txt") as work_data: #hardcoded filename :/
    for line in work_data:
        if line.rstrip('\n') == "*" or line == "\n":
            #print("pass") debugged
            continue
        if True: #I know how it looks, sorry
            note = {'deckName': 'test1', 'modelName': 'Basic', 'fields': {'Front': line, 'Back': translator.translate(line)}, 'options': { 'allowDuplicate': True, 'duplicateScope': 'deck'}}
            invoke('addNote', note=note)
            #print(line) debugged
