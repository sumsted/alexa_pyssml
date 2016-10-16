from bottle import get, post, request
from pyssml.PySSML import PySSML

from logit import logit


@get('/')
def get_index():
    return 'alexa pyssml'


@post('/alexa/event')
def post_alexa_event():
    result = {}
    alexa_event = request.json
    alexa_request = alexa_event['request'] if 'request' in alexa_event else None
    alexa_session = alexa_event['session'] if 'session' in alexa_event else None
    logit('alexa_event: %s' % str(alexa_event))

    if alexa_session['new']:
        logit('New Session: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))

    if alexa_request['type'] == "LaunchRequest":
        logit('LaunchRequest: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
        return {"welcome"}

    elif alexa_request['type'] == "IntentRequest":
        logit('IntentRequest: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
        return route_intent(alexa_request, alexa_session)

    elif alexa_request['type'] == "SessionEndedRequest":
        logit('SessionEndedRequest: requestId: %s, sessionId: %s' %
              (str(alexa_request['requestId']), str(alexa_session['sessionId'])))
    return result


def route_intent(alexa_request, alexa_session):
    intent = alexa_request['intent']
    intent_name = intent['name']
    return INTENT_HANDLERS[intent_name](intent, alexa_session)


def handle_story_intent(intent, alexa_session):
    s = PySSML()
    s.paragraph("Once upon a time there was an old woman who loved baking gingerbread. She would bake gingerbread cookies, cakes, houses and gingerbread people, all decorated with chocolate and peppermint, caramel candies and colored frosting.")
    s.pause("200ms")
    s.say("Give me a")
    s.spell_slowly("Tigers", "100ms")
    s.say("Go Tigers!")

    result = {
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
            'outputSpeech': s.to_object(),
            'card': {
                'type': 'Simple',
                'title': 'Story',
                'content': s.card()
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'Are you there?'
                }
            },
            'shouldEndSession': False
        }
    }
    return result


INTENT_HANDLERS = {
    'storyIntent': handle_story_intent
}

